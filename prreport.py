import datetime
import json
import re
import urllib.request
from urllib.error import HTTPError
import sys
import time

PER_PAGE=100 # github limit
HTTP_ERROR_RETRY_SLEEP=10 # in seconds

def get_owner_repo(url: str) -> (str, str):
    [owner, repo] = re.findall(r'https://github.com/(.*)/(.*)', url)[0]
    return owner, repo

def get_prs_api_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    [owner, repo] = get_owner_repo(url)
    return f'https://api.github.com/search/issues?per_page={PER_PAGE}&q=repo:{owner}/{repo}+merged:{date_start.strftime("%Y-%m-%d")}..{date_end.strftime("%Y-%m-%d")}'


def get_prs_browsable_url(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    return url+f'/pulls?q=merged:{date_start.strftime("%y-%m-%d")}..{date_end.strftime("%y-%m-%d")}'


# https://api.github.com/search/issues?q=repo:oasisprotocol/docs+merged:2024-05-01..2024-05-31
def pr_report(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    prs_url = get_prs_api_url(url, date_start, date_end)
    print(f'Fetching {prs_url}', file=sys.stderr)
    [_, repo] = get_owner_repo(url)

    raw_json = ''
    while raw_json == '':
        try:
            raw_json = urllib.request.urlopen(prs_url)
        except HTTPError as e:
            print(f'HTTP error: {e.code}, retrying...', file=sys.stderr)
            time.sleep(HTTP_ERROR_RETRY_SLEEP)

    prs = json.load(raw_json)
    if len(prs.items) == 0:  # Skip the section, if no PRs merged this month.
        return ''

    out = ''
    out += f'<p>The <a href="{url}">{repo}</a> team merged the following PRs this month:\n'
    out += '<ol>\n'
    for pr in prs['items']:
        out += f'<li>{pr["title"]} (<a href="{pr["url"]}">#{pr["number"]}</a>)'
        if not pr["body"] is None:
            out += f'<br/>{pr["body"]}'
        out += '</li>'
    out += '</ol></p>'

    prs_burl = get_prs_browsable_url(url, date_start, date_end)
    out += f'<p>In total, <a href="{prs_burl}">{prs["total_count"]} pull requests</a> were merged this month.</p>'
    return out
