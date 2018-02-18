# coding:utf-8
"""Test for tglp.api."""
from datetime import date

import pytest

from tglp.api import TogglAPI


@pytest.fixture
def api():
    """Create api object using among tests."""
    pseudo_workspace_id = 1234567
    return TogglAPI('pseudo_api_token', pseudo_workspace_id, '2017-01-01')


def test_query_in_alive_network(api):
    """Check if _query returns json response."""
    report = api._query('2017-01-01', '2017-12-31')
    assert isinstance(report, dict)


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
