# coding:utf-8
"""A wrapper of Toggl API."""
import sys
from datetime import date
from datetime import timedelta

import requests
from requests.auth import HTTPBasicAuth


class TogglAPI:
    """A wrapper of Toggl API."""

    def __init__(self, api_token, workspace_id, aggregation_begin):
        """Set api_token, workspace id and since."""
        self._api_token = api_token
        self._workspace_id = workspace_id
        self._aggregation_begin = aggregation_begin

    def _query(self, since, until):
        """Call Toggl API actually."""
        url = 'https://toggl.com/reports/api/v2/summary'
        params = {
            'workspace_id': self._workspace_id,
            'user_agent': 'Togglepo',
            'since': since,
            'until': until
        }

        try:
            report = requests.get(
                url,
                params=params,
                auth=HTTPBasicAuth(self._api_token, 'api_token')
            )
        except requests.exceptions.ConnectionError:
            sys.stderr.write('Failed to connect to api server.\n')
            sys.exit(1)

        return report.json()

    def _divide_elapsed_span(self, until=date.today()):
        """Divide span (today - aggregation_begin) to adjust to Toggl API."""
        since = date(*map(int, self._aggregation_begin.split('-')))
        years = list()
        date_format = '%Y-%m-%d'
        while True:
            # Maximum date span of Toggl API is 1 year.
            # Use it as interval to minimize the number of execution of _query.
            if (until - since).days <= 365:
                year = dict(
                    since=date.strftime(since, date_format),
                    until=date.strftime(until, date_format)
                )
                years.append(year)
                return years
            else:
                after_one_year_from_since = since + timedelta(days=365)
                year = dict(
                    since=date.strftime(since, date_format),
                    until=date.strftime(after_one_year_from_since, date_format)
                )
                years.append(year)
                since = after_one_year_from_since + timedelta(days=1)

    def total_time_entries(self):
        """Aggregate time entry of all years."""
        total = dict()
        years = self._divide_elapsed_span()

        for year in years:
            report = self._query(**year)
            for datum in report['data']:
                prj = datum['title']['project']
                time_sec = datum['time'] / 1000
                total[prj] = total.get(prj, 0) + time_sec
        return total
