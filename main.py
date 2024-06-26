#!/bin/python3

import sys
import calendar
import datetime
import re

from prreport import pr_report
from txreport import tx_report

date_start: datetime.date
date_end: datetime.date


def print_usage():
    print("Monthly report generator. Usage:")
    print("repgen <YYYY-MM>")


def main():
    global date_start, date_end
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    year = int(sys.argv[1][0:4])
    month = int(sys.argv[1][5:])
    date_start = datetime.date(year, month, 1)
    date_end = datetime.date(year, month, calendar.monthrange(year, month)[1])

    f = open("template.html", "r")
    tpl = f.read()

    tpl = tpl.replace("{{MONTH}}", date_start.strftime("%b"))
    tpl = tpl.replace("{{YEAR}}", str(year))

    pr_reports = re.findall(r'{{PR_REPORT (.*)}}', tpl)
    for prr in pr_reports:
        tpl = tpl.replace(r'{{PR_REPORT '+prr+'}}', pr_report(prr, date_start, date_end))

    tx_reports = re.findall(r'{{TX_REPORT (.*)}}', tpl)
    for txr in tx_reports:
        tpl = tpl.replace(r'{{TX_REPORT '+txr+'}}', tx_report(txr, date_start, date_end))

    print(tpl)


if __name__ == "__main__":
    main()
