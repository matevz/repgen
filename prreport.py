from base64 import b64encode
import datetime
import json
import re
import urllib.request
from urllib.error import HTTPError
import os
import sys
import time

PER_PAGE = 100  # github limit
HTTP_ERROR_RETRY_SLEEP = 10  # in seconds
IGNORE_DIFF_FILES = ['go.sum', ' Cargo.lock', 'package.lock', 'yarn.lock', 'pnpm-lock.yaml', '.svg', '.tsx.snap',
                     '.body', '.headers']


def extract_public_repo_urls(regex: str) -> list:
    """Detects, if a single URL or regex for multiple repositories is provided. Looks up the repo(s) and returns the
    URL(s) of public repositories that can be scraped."""
    if '*' not in regex:
        return [regex]

    [owner, repo] = get_owner_repo(regex)
    repo = repo.replace('*', '')  # Asterisk is not supported inside github queries.
    repos_query_url = f'https://api.github.com/search/repositories?per_page={PER_PAGE}&q={repo}+in:name+org:{owner}'
    repos = json.load(fetch(repos_query_url))
    html_urls = []
    for repo in repos['items']:
        if not repo['private']:
            html_urls.append(repo['html_url'])
    return html_urls


def get_owner_repo(url: str) -> (str, str):
    [owner, repo] = re.findall(r'https://github.com/(.*)/(.*)', url)[0]
    return owner, repo


def get_prs_api_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    [owner, repo] = get_owner_repo(url)
    return f'https://api.github.com/search/issues?per_page={PER_PAGE}&q=repo:{owner}/{repo}+merged:{date_start.strftime("%Y-%m-%d")}..{date_end.strftime("%Y-%m-%d")}'


def get_prs_browsable_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    return url + f'/pulls?q=merged:{date_start.strftime("%Y-%m-%d")}..{date_end.strftime("%Y-%m-%d")}'


def compute_relevant_diff(diff: str) -> int:
    block = re.findall(r'\n---\n(.*)\n---\s.+', diff, re.DOTALL)
    sum = 0
    if len(block) == 0:
        return sum

    for line in block[0].split('\n'):
        split_line = line.split('|')
        if len(split_line) != 2 or len(split_line[1].split()) != 2:
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
    """Fetch the GitHub resource requiring API_KEY."""
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


def fetch_diffs(items):
    """Populates PRs with their raw diffs."""
    for i, pr in enumerate(items):
        res = fetch(pr['pull_request']['patch_url'])
        pr['raw_diff'] = res.read().decode(res.headers.get_content_charset())


def reorder_prs_by_diff(items):
    """Reorders the given PRs by their relevant diff. Requires populated raw_diff."""
    diff_amt = []

    for i, pr in enumerate(items):
        diff_len = compute_relevant_diff(pr['raw_diff'])
        diff_amt.append((diff_len, i))

    new_items = []
    diff_amt.sort(reverse=True)
    for amt, i in diff_amt:
        items[i]['diff'] = amt
        new_items.append(items[i])

    return new_items


def fetch_changelogs(items):
    """Fetches the changelogs from PR diffs. Requires populated raw_diff."""
    for pr in items:
        query = r'\n\+\+\+\ b\/\.changelog\/' + str(pr['number']) + r'\.[a-z]+\.md\n@@[\+\-\,\ 0-9]+@@\n(.*)'
        blocks = re.findall(query, pr['raw_diff'], re.DOTALL)
        if len(blocks) != 1 or blocks[0] == '' or blocks[0] == '\n':
            continue

        pr['changelog'] = ''
        blocks[0] = blocks[0].replace('\n+\n', '<br/>\n')
        for b in blocks[0].split('\n'):
            # + should be the first character in the diff
            if len(b) > 0 and b[0] == '+':
                pr['changelog'] += b[1:] + ' '
            else:
                break


def fetch_images(items):
    """Fetches images and embeds them inside the body_html."""
    queries = [r'\<img src="(http[^"]*)"', r'\<video src="(http[^"]*)"']
    for pr in items:
        if not 'body_html' in pr or pr['body_html'] is None:
            continue

        for q in queries:
            match = re.search(q, pr['body_html'])
            while match != None:
                url = match.groups()[0]
                res = ''
                print(f'Fetching {url}', file=sys.stderr)
                while res == '':
                    try:
                        res = urllib.request.urlopen(url)
                    except HTTPError as e:
                        print(f'HTTP error: {e.code}, retrying...', file=sys.stderr)
                        time.sleep(HTTP_ERROR_RETRY_SLEEP)

                inlineSrc = f'data:{res.headers["Content-Type"]};base64, {b64encode(res.read()).decode("utf-8")}'
                pr['body_html'] = pr['body_html'].replace(match.groups()[0], inlineSrc)
                match = re.search(q, pr['body_html'])


def get_releases_tags(url: str, date_start: datetime.date, date_end: datetime.date) -> list:
    """Obtains any releases made this month and tags, if not covered by releases."""
    [owner, repo] = get_owner_repo(url)
    releases_url = f'https://api.github.com/repos/{owner}/{repo}/releases?per_page={PER_PAGE}'
    releases = json.load(fetch(releases_url))
    relevant_releases = []
    for r in releases:
        if 'published_at' not in r or r['published_at'] is None:
            continue
        published = datetime.datetime.fromisoformat(r['published_at'][:-1]).date()  # trim Z suffix
        if date_start <= published <= date_end:
            relevant_releases.append(r)

    tags_url = f'https://api.github.com/repos/{owner}/{repo}/tags?per_page={PER_PAGE}'
    tags = json.load(fetch(tags_url))
    relevant_tags = []
    for t in tags:
        found = False
        for r in releases:
            if t["name"] == r["tag_name"]:
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
    """Generates a PR report for a repository with a specified URL."""
    prs_url = get_prs_api_url(url, date_start, date_end)
    print(f'Fetching {prs_url}', file=sys.stderr)
    [_, repo] = get_owner_repo(url)

    prs = json.load(fetch(prs_url))
    if len(prs['items']) == 0:  # Skip the section, if no PRs merged this month.
        return ''

    fetch_images(prs['items'])
    fetch_diffs(prs['items'])
    fetch_changelogs(prs['items'])
    prs['items'] = reorder_prs_by_diff(prs['items'])

    team = repo.split('-')
    team = [t.capitalize() for t in team]
    team = ' '.join(team)

    out = ''
    out += f'<h3>{team}</h3>\n'
    out += f'<p>The <b><a href="{url}">{team}</a></b> team merged {prs["total_count"]} PRs this month:\n'
    for pr in prs['items']:
        if 'dependabot' in pr["user"]["login"] or 'renovate' in pr["user"]["login"]:
            continue
        out += '<div>\n'
        out += f'<input type="checkbox" /> {pr["title"]} (<a href="{pr["html_url"]}">#{pr["number"]}</a>) <b><a href="{pr["html_url"]}/files">±{pr["diff"]}</a></b> by <b>{pr["user"]["login"]}</b> @ {pr["pull_request"]["merged_at"][0:10]}.\n'
        if 'body_html' in pr and not pr['body_html'] is None:
            out += f'<div class="pr_desc">{pr["body_html"]}</div>'
        if 'changelog' in pr:
            out += '<div class="pr_changelog">'
            out += '<p class="pr_changelog_title">CHANGELOG:</p>\n'
            out += f'<p>{pr["changelog"]}</p>'
            out += '\n</div>'
        out += '</div>\n'

    releases = get_releases_tags(url, date_start, date_end)
    if len(releases) > 0:
        out += f'{len(releases)} new releases of {repo} were made this month:\n<ul>\n'
        for r in sorted(releases, key=lambda release: release["tag_name"]):
            published = datetime.datetime.fromisoformat(r["published_at"][:-1]).date()
            out += f'<li>'
            out += f'<b><a href="{r["html_url"]}">{r["tag_name"]}</a></b> released on {published.strftime("%B %-d")}.'
            if 'body_html' in r and not r['body_html'] is None:
                out += f'<div class="pr_desc">{r["body_html"]}</div>'
            out += '</li>\n'
        out += f'</ul>\n'

    prs_burl = get_prs_browsable_url(url, date_start, date_end)
    out += f'In total, <a href="{prs_burl}">{prs["total_count"]} pull requests</a> were merged in {date_start.strftime("%B")}.</p><hr/>'
    return out
