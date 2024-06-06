import calendar
import csv
import datetime
import sys
import urllib


def get_network_paratime(url: str) -> (str, str):
    filename = url.split('/')[-1]
    chunks = filename.split('_')
    return chunks[0].capitalize(), chunks[1].capitalize()


def format_url(url: str, date_start: datetime.date):
    url = url.replace('%Y', date_start.strftime("%Y"))
    url = url.replace('%m', date_start.strftime("%m"))
    return url


def get_prev_month(date_start: datetime.date) -> (datetime.date, datetime.date):
    new_date_start = date_start - datetime.timedelta(days = 1)
    new_date_start = new_date_start.replace(day = 1)

    new_date_end = new_date_start.replace(day = calendar.monthrange(new_date_start.year, new_date_start.month)[1])
    return new_date_start, new_date_end

def compute_max(txes: list, date_start: datetime.date, date_end: datetime.date) -> (int, int, datetime.date, datetime.date):
    min_txes = sys.maxsize
    min_date = 0
    max_txes = 0
    max_date = 0
    for row in txes:
        curDate = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()
        if date_start <= curDate <= date_end and min_txes > int(row['all']):
            min_txes = int(row['all'])
            min_date = curDate
        if date_start <= curDate <= date_end and max_txes < int(row['all']):
            max_txes = int(row['all'])
            max_date = curDate
    return min_txes, max_txes, min_date, max_date

def compute_average(txes: list, date_start: datetime.date, date_end: datetime.date) -> float:
    avg = 0.0
    count = 0
    for row in txes:
        curDate = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()
        if date_start <= curDate <= date_end:
            avg += float(row['all'])
            count += 1
    avg /= count
    return avg


def import_csv(url: str) -> list:
    """XXX: poorman's CSV parser. Use csv.DictReader() instead."""
    raw_csv = urllib.request.urlopen(url).read().decode('utf-8')
    lines = raw_csv.splitlines()
    if len(lines)<1:
        return []
    fields = lines[0].split(',')
    res = []
    for line in lines[1:]:
        d_val = {}
        for i,val in enumerate(line.split(',')):
            d_val[fields[i]] = val
        res.append(d_val)

    return res


def tx_report(url: str, date_start: datetime.date, date_end: datetime.date) -> str:
    network, paratime = get_network_paratime(url)

    fetch_url = format_url(url, date_start)
    tx_stats = import_csv(fetch_url)
    monthly_min, monthly_max, monthly_min_date, monthly_max_date = compute_max(tx_stats, date_start, date_end)
    monthly_avg = compute_average(tx_stats, date_start, date_end)

    prev_date_start, prev_date_end = get_prev_month(date_start)
    prev_fetch_url = format_url(url, prev_date_start)
    prev_tx_stats = import_csv(prev_fetch_url)
    prev_monthly_min, prev_monthly_max, prev_monthly_min_date, prev_monthly_max_date = compute_max(prev_tx_stats, prev_date_start, prev_date_end)
    prev_monthly_avg = compute_average(prev_tx_stats, prev_date_start, prev_date_end)

    out = '<p>'
    out += f'The number of daily transactions on <b>{paratime} {network}</b> fluctuated between {monthly_min} and {monthly_max}. '
    out += (f'The monthly average in {date_start.strftime("%b")} was <b>{round(monthly_avg)}</b> transactions per day and was '
           f'{round(abs((monthly_avg/prev_monthly_avg)*100 - 100))}% {"higher" if monthly_avg>prev_monthly_avg else "lower"} compared to '
           f'the last month ({round(prev_monthly_avg)} transactions). ')
    out += (f'The daily maximum was <b>{monthly_max}</b> transactions on {monthly_max_date.strftime("%d %b")} (compared '
            f'to {prev_monthly_max} the last month on {prev_monthly_max_date.strftime("%d %b")}).')
    out += '</p>'

    return out