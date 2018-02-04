# coding:utf-8
"""A wrapper of Toggl API."""
import sys

import requests
from requests.auth import HTTPBasicAuth


class TogglAPI:
    """A wrapper of Toggl API."""

    def __init__(self, api_token, workspace_id):
        """Set api_token and workspace_id."""
        self._api_token = api_token
        self._workspace_id = workspace_id

    def _query(self, since, until):
        """Call Toggl API actually."""
        url = 'https://toggl.com/reports/api/v2/summary'
        params = {
            'workspace_id': self._workspace_id,
            'user_agent': 'Togglepo',
            # maximum date span (until - since) is 1 year.
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

    def total_time_entries(self, years):
        """Aggregate time entry of all years."""
        total = dict()

        for year in years:
            report = self._query(**year)
            for datum in report['data']:
                prj = datum['title']['project']
                time_sec = datum['time'] / 1000
                total[prj] = total.get(prj, 0) + time_sec
        return total
