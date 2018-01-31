# coding:utf-8
import sys
from datetime import datetime

from dateutil.relativedelta import relativedelta

import requests
from requests.auth import HTTPBasicAuth


class TogglAPI:
    """A wrapper of Toggl API."""

    def __init__(self, api_token, workspace_id):
        """Set api_token and workspace_id as instance variables."""
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
            r = requests.get(
                url,
                params=params,
                auth=HTTPBasicAuth(self._api_token, 'api_token')
            )
        except requests.exceptions.ConnectionError:
            sys.stderr.write('Failed to connect to api server.')
            sys.stderr.write('Please check your network.')
            sys.stderr.write('See "tglp --help" for more details.')
            sys.exit(1)

        return r.json()

    def get_time_entries(self, since):
        """Get time entries from since to today."""
        time_entries = list()
        while True:
            since_dt = datetime.strptime(since, '%Y-%m-%d')
            after_1_year_from_since_dt = since_dt + relativedelta(years=1)
            after_1_year_from_since = datetime.strftime(
                after_1_year_from_since_dt,
                '%Y-%m-%d'
            )
            entries = self._query(since, after_1_year_from_since)
            time_entries.extend(entries['data'])

            if datetime.today() <= after_1_year_from_since_dt:
                return time_entries
            else:
                since = after_1_year_from_since
