import datetime
import json
import re
import urllib.request
from urllib.error import HTTPError
import os
import sys
import time

PER_PAGE=100 # github limit
HTTP_ERROR_RETRY_SLEEP=10 # in seconds
IGNORE_DIFF_FILES=['go.sum',' Cargo.lock', 'package.lock', 'yarn.lock', 'pnpm-lock.yaml', '.svg', '.tsx.snap']


def get_owner_repo(url: str) -> (str, str):
    [owner, repo] = re.findall(r'https://github.com/(.*)/(.*)', url)[0]
    return owner, repo


def get_prs_api_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    [owner, repo] = get_owner_repo(url)
    return f'https://api.github.com/search/issues?per_page={PER_PAGE}&q=repo:{owner}/{repo}+merged:{date_start.strftime("%Y-%m-%d")}..{date_end.strftime("%Y-%m-%d")}'


def get_prs_browsable_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    return url+f'/pulls?q=merged:{date_start.strftime("%Y-%m-%d")}..{date_end.strftime("%Y-%m-%d")}'


def format_body(body: str) -> str:
    """Formats the PR body in Markdown."""
    return body.replace("\r\n", "<br/>\n")

def compute_relevant_diff(diff: str) -> int:
    block = re.findall(r'\n---\n(.*)\n---\s.+', diff, re.DOTALL)
    sum = 0
    if len(block) == 0:
        return sum

    for line in block[0].split('\n'):
        split_line = line.split('|')
        if len(split_line)!=2 or len(split_line[1].split())!=2:
            continue
        if not split_line[1].split()[0].isdigit():
            continue
        ignore = False
        for ig in IGNORE_DIFF_FILES:
            if ig in split_line[0]:
                ignore = True
        if ignore:
            continue
        sum += int(split_line[1].split()[0])
    return sum

def fetch(url: str) -> str:
    print(f'Fetching {url}', file=sys.stderr)
    res = ''
    while res == '':
        try:
            req = urllib.request.Request(url)
            req.add_header('Accept', 'application/vnd.github.full+json')
            if 'API_KEY' in os.environ:
                req.add_header('Authorization', f'Bearer {os.environ["API_KEY"]}')
            res = urllib.request.urlopen(req)
        except HTTPError as e:
            print(f'HTTP error: {e.code}, retrying...', file=sys.stderr)
            time.sleep(HTTP_ERROR_RETRY_SLEEP)

    return res

def reorder_prs_by_diff(items):
    diff_amt = []

    for i,pr in enumerate(items):
        res = fetch(pr['pull_request']['patch_url'])
        diff = res.read().decode(res.headers.get_content_charset())
        diff_len = compute_relevant_diff(diff)
        diff_amt.append((diff_len, i))

    new_items = []
    diff_amt.sort(reverse=True)
    for amt,i in diff_amt:
        items[i]['diff'] = amt
        new_items.append(items[i])

    return new_items


def get_releases_tags(url: str, date_start: datetime.date, date_end: datetime.date) -> list:
    """Obtains any releases made this month and tags, if not covered by releases."""
    [owner, repo] = get_owner_repo(url)
    releases_url = f'https://api.github.com/repos/{owner}/{repo}/releases'
    releases = json.load(fetch(releases_url))
    relevant_releases = []
    for r in releases:
        if 'published_at' not in r or r['published_at'] is None:
            continue
        published = datetime.datetime.fromisoformat(r['published_at'][:-1]).date()  # trim Z suffix
        if date_start <= published <= date_end:
            relevant_releases.append(r)

    tags_url = f'https://api.github.com/repos/{owner}/{repo}/tags'
    tags = json.load(fetch(tags_url))
    relevant_tags = []
    for t in tags:
        found = False
        for r in releases:
            if t["name"]==r["tag_name"]:
                found = True
                break
        if not found:
            relevant_tags.append(t)

    for t in relevant_tags:
        c = json.load(fetch(t["commit"]["url"]))
        published = datetime.datetime.fromisoformat(c["commit"]["author"]["date"][:-1]).date()
        if date_start <= published <= date_end:
            t["html_url"] = f'https://github.com/{owner}/{repo}/releases/tag/{t["name"]}'
            t["published_at"] = c["commit"]["author"]["date"]
            t["tag_name"] = t["name"]
            relevant_releases.append(t)
    return relevant_releases

def pr_report(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    prs_url = get_prs_api_url(url, date_start, date_end)
    print(f'Fetching {prs_url}', file=sys.stderr)
    [_, repo] = get_owner_repo(url)

    prs = json.load(fetch(prs_url))
    if len(prs['items']) == 0:  # Skip the section, if no PRs merged this month.
        return ''

    prs['items'] = reorder_prs_by_diff(prs['items'])

    out = ''
    out += f'<p>The <a href="{url}">{repo}</a> team merged the following PRs this month:\n'
    for pr in prs['items']:
        if 'dependabot' in pr["user"]["login"] or 'renovate' in pr["user"]["login"]:
            continue
        out += '<p>\n'
        out += f'{pr["title"]} (<a href="{pr["html_url"]}">#{pr["number"]}</a>) <b>±{pr["diff"]}</b> by <b>{pr["user"]["login"]}</b> @ {pr["pull_request"]["merged_at"][0:10]}'
        if 'body_html' in pr and not pr['body_html'] is None:
            out += f'.\n<div class="pr_desc">{pr["body_html"]}</div>'
        out += '</p>\n'

    releases = get_releases_tags(url, date_start, date_end)
    if len(releases)>0:
        out += f'{len(releases)} new releases of {repo} were made this month:\n<ul>\n'
        for r in releases:
            published = datetime.datetime.fromisoformat(r["published_at"][:-1]).date()
            out += f'<li>'
            out += f'<a href="{r["html_url"]}">{r["tag_name"]}</a> released on {published.strftime("%b %d")}.'
            if 'body_html' in r and not r['body_html'] is None:
                out += f'<br/>{r["body_html"]}'
            out += '</li>\n'
        out += f'</ul>\n'

    prs_burl = get_prs_browsable_url(url, date_start, date_end)
    out += f'In total, <a href="{prs_burl}">{prs["total_count"]} pull requests</a> were merged in {date_start.strftime("%b")}.</p>'
    return out
