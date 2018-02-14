# coding:utf-8
"""Test for tglp.api."""
import pytest
from datetime import date

from tglp.api import TogglAPI


@pytest.fixture
def api():
    """Create api object using among tests."""
    pseudo_workspace_id = 1234567
    return TogglAPI('pseudo_api_token', pseudo_workspace_id, '2016-01-01')


def test_divide_elapsed_span_within_one_year(api):
    divided_span = api._divide_elapsed_span(today_date=date(2016, 12, 31))
    assert divided_span == [{'since': '2016-01-01', 'until': '2016-12-31'}]

def test_divide_elapsed_span_over_one_year(api):
    divided_span = api._divide_elapsed_span(today_date=date(2018, 2, 14))
    assert divided_span == [
        {'since': '2016-01-01', 'until': '2017-01-01'},
        {'since': '2017-01-02', 'until': '2018-01-02'},
        {'since': '2018-01-03', 'until': '2018-02-14'},
    ]
