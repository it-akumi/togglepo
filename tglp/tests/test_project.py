# coding:utf-8
"""Test for tglp.project."""
import pytest

from tglp.project import Project


@pytest.fixture
def project():
    """Create project object using among tests."""
    return Project('test_project', 50)


@pytest.fixture
def time_entries():
    """Create time_entries object using among tests."""
    return {'test_project': 12.21 * 3600, 'pseudo_project': 1000}


def test_set_achieved_sec(project, time_entries):
    """Check if achieved_sec is set correctly."""
    project.set_achieved_sec(time_entries)
    assert project._achieved_sec == 12.21 * 3600


def test_get_achievement_rate(project, time_entries):
    """Check if achievement_rate is calculated correctly."""
    project.set_achieved_sec(time_entries)
    assert project.get_achievement_rate() == '24.42%'


def test_normalized_achieved_sec(project, time_entries):
    """Check if project._achieved_sec is normalized."""
    project.set_achieved_sec(time_entries)
    assert project.normalized_achieved_sec() == '   12h 12m 36s'
