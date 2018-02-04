# coding:utf-8
"""Calculate each period of a project."""
from datetime import date

from dateutil.relativedelta import relativedelta


class Period:
    """Calculate each period of a project."""

    def __init__(self, begin, end):
        """Set project beginning date and end date."""
        self._begin_date = date(*map(int, begin.split('-')))
        self._end_date = date(*map(int, end.split('-')))

    def remaining_days(self):
        """Project remaining days."""
        remaining = (self._end_date - date.today()).days
        return remaining

    def divide_passed_period(self):
        """Divide project passed period into years."""
        years = list()
        since = self._begin_date
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
