# coding:utf-8
import sys

import requests
from requests.auth import HTTPBasicAuth


class TogglAPI:
    """A wrapper of Toggl API."""

    def __init__(self, api_token, workspace_id):
        """Set api_token and workspace_id as instance variables."""
        self.api_token = api_token
        self.workspace_id = workspace_id

    def _query(self, since, until):
        """Get aggregated time entries from since to until."""
        url = 'https://toggl.com/reports/api/v2/summary'
        params = {
            'workspace_id': self.workspace_id,
            'since': since,
            'until': until,
            'user_agent': 'Togglepo'
        }

        try:
            r = requests.get(
                url,
                params=params,
                auth=HTTPBasicAuth(self.api_token, 'api_token')
            )
        except requests.exceptions.ConnectionError:
            sys.stderr.write('Failed to connect to api server.')
            sys.stderr.write('Please check your network.')
            sys.stderr.write('See "tglp --help" for more details.')
            sys.exit(1)

        return r.json()

    def get_time_entries(since, until):
        """Get time entries over 1 year and return aggregated result."""
        pass
