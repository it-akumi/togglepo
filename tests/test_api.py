# coding:utf-8
"""Test for tglp.api."""
from datetime import date
from unittest.mock import patch

import pytest

import requests

from tglp.api import TogglAPI


@pytest.fixture
def api():
    """Create api object using among tests."""
    pseudo_workspace_id = 1234567
    return TogglAPI('pseudo_api_token', pseudo_workspace_id, '2017-01-01')


@patch('requests.get')
def test_query_in_alive_network(mock_requests_get, api):
    """Check if _query returns json response."""
    mock_requests_get.return_value.json.return_value = {}
    report = api._query(since='2017-01-01', until='2017-12-31')
    assert isinstance(report, dict)


@patch('requests.get')
def test_query_in_dead_network(mock_requests_get, api):
    """exit(1) if _query raises requests.exceptions.ConnectionError."""
    mock_requests_get.side_effect = requests.exceptions.ConnectionError
    with pytest.raises(SystemExit):
        api._query(since='2017-01-01', until='2017-12-31')


@patch('requests.get')
def test_query_when_api_returns_errors(mock_requests_get, api):
    """exit(1) if Toggl API returns 4xx."""
    # When AGGREGATION_BEGIN is invalid
    mock_requests_get.return_value.status_code = 400
    with pytest.raises(SystemExit):
        api._query(since='1000-01-01', until='1000-12-31')

    # When API_TOKEN is invalid
    mock_requests_get.return_value.status_code = 401
    with pytest.raises(SystemExit):
        api._query(since='2017-01-01', until='2017-12-31')

    # When WORKSPACE_ID is invalid
    mock_requests_get.return_value.status_code = 403
    with pytest.raises(SystemExit):
        api._query(since='2017-01-01', until='2017-12-31')


def test_divide_elapsed_span_within_one_year(api):
    """Check if _divide_elapsed_span returns one year itself."""
    divided_span = api._divide_elapsed_span(until=date(2017, 12, 31))
    assert divided_span == [{'since': '2017-01-01', 'until': '2017-12-31'}]


def test_divide_elapsed_span_over_one_year_not_including_leap_year(api):
    """Check if span over one year is divided correctly."""
    divided_span = api._divide_elapsed_span(until=date(2018, 2, 15))
    assert divided_span == [
        {'since': '2017-01-01', 'until': '2018-01-01'},
        {'since': '2018-01-02', 'until': '2018-02-15'},
    ]


def test_divide_elapsed_span_over_one_year_including_leap_year(api):
    """Check if span including leap year is divided correctly."""
    divided_span = api._divide_elapsed_span(until=date(2021, 12, 31))
    assert divided_span == [
        {'since': '2017-01-01', 'until': '2018-01-01'},
        {'since': '2018-01-02', 'until': '2019-01-02'},
        {'since': '2019-01-03', 'until': '2020-01-03'},
        # 2020 is leap year.
        {'since': '2020-01-04', 'until': '2021-01-03'},
        {'since': '2021-01-04', 'until': '2021-12-31'},
    ]
