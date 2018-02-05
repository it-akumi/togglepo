# coding:utf-8
"""Manage project goal."""
import sys


class Goal:
    """Manage project goal."""

    def __init__(self, goal_h, achieved_sec):
        """Set goal and achieved as seconds."""
        if goal_h == 0:
            sys.stderr.write('Goal NOT allowed to be 0\n')
            sys.exit(1)
        self._goal = goal_h * 3600
        self._achieved = achieved_sec

    def daily_goal(self, remaining_days, max_daily_working_hours):
        """Daily goal for goal achievement in remaining days."""
        if remaining_days <= 0:
            return None

        daily_goal = self._goal / remaining_days
        if daily_goal > max_daily_working_hours * 3600:
            return None
        else:
            return daily_goal

    def achievement_rate(self):
        """Achievement rate in percent."""
        return (self._achieved / self._goal) * 100
