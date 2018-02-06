# coding:utf-8
"""Date calculation."""
from datetime import date

from dateutil.relativedelta import relativedelta


def divide_elapsed_span(begin):
    """Divide elapsed span of a project into years."""
    begin_date = date(*map(int, begin.split('-')))
    years = list()
    since = begin_date
    date_format = '%Y-%m-%d'
    while True:
        one_year_passed = since + relativedelta(years=1)
        if date.today() <= one_year_passed:
            year = dict(
                since=date.strftime(since, date_format),
                until=date.strftime(date.today(), date_format)
            )
            years.append(year)
            return years
        else:
            year = dict(
                since=date.strftime(since, date_format),
                until=date.strftime(one_year_passed, date_format)
            )
            years.append(year)
            since = one_year_passed + relativedelta(days=1)


def remaining_days(end):
    """Remaining days of a project."""
    end_date = date(*map(int, end.split('-')))
    remaining = (end_date - date.today()).days
    return remaining
