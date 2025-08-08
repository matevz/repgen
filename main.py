#!/bin/python3

import argparse
import sys
import calendar
import datetime
import re

from prreport import pr_report, extract_public_repo_urls
from txreport import tx_report
from discordreport import get_chats
from template import Template

date_start: datetime.date
date_end: datetime.date


def main():
    global date_start, date_end

    parser = argparse.ArgumentParser()
    parser.add_argument('date', help='Date in YYYY-MM format')
    parser.add_argument('-o', '--output', help='Output file name (default: stdout)')
    parser.add_argument('-t', '--template', default='template.html', help='Template file name (default: template.html)')
    parser.description = '''Monthly report generator.
  
environment variables:
  API_KEY: Github API key to avoid rate limits
  DISCORD_TOKEN: To read announcements'''
    parser.formatter_class = argparse.RawDescriptionHelpFormatter
    parser.epilog = 'Example: repgen 2024-01'

    args = parser.parse_args()

    # Validate date format
    if not re.match(r'^\d{4}-\d{2}$', args.date):
        print("Error: Date must be in YYYY-MM format")
        sys.exit(1)

    year = int(args.date[0:4])
    month = int(args.date[5:])
    date_start = datetime.date(year, month, 1)
    date_end = datetime.date(year, month, calendar.monthrange(year, month)[1])

    tpl = Template(args.template, args.output)

    tpl.replace("{{MONTH}}", date_start.strftime("%B"))
    tpl.replace("{{YEAR}}", str(year))

    # Generate repositories report based on merged PRs.
    pr_reports = re.findall(r'{{PR_REPORT (.*)}}', tpl.content)
    # Replace any URL regex with direct repo URL.
    for prr in pr_reports:
        single_urls = ''
        for single_prr in extract_public_repo_urls(prr):
            single_urls += '{{PR_REPORT ' + single_prr + '}}\n'
        tpl.replace('{{PR_REPORT ' + prr + '}}', single_urls)
    # Generate the actual PR report.
    pr_reports = re.findall(r'{{PR_REPORT (.*)}}', tpl.content)
    for prr in pr_reports:
        tpl.replace(r'{{PR_REPORT '+prr+'}}', pr_report(prr, date_start, date_end))

    # Generate transaction statistics report.
    tx_reports = re.findall(r'{{TX_REPORT (.*)}}', tpl.content)
    for txr in tx_reports:
        tpl.replace(r'{{TX_REPORT '+txr+'}}', tx_report(txr, date_start, date_end))

    # Generate transaction statistics report.
    discord_reports = re.findall(r'{{DISCORD_REPORT (.*)}}', tpl.content)
    for channel_id in discord_reports:
        tpl.replace(r'{{DISCORD_REPORT '+channel_id+'}}', get_chats(int(channel_id), date_start, date_end))

    if not args.output:
        print(tpl)


if __name__ == "__main__":
    main()
