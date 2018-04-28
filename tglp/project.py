# coding:utf-8
"""Project attributes."""


class Project:
    """Calculate values related to each project."""

    def __init__(self, name, goal_h):
        """Set project attributes."""
        self.name = name
        self.goal_h = goal_h
        self._achieved_sec = 0

    def set_achieved_sec(self, total_time_entries):
        """Set to 0 sec if project is not found."""
        self._achieved_sec = total_time_entries.get(self.name, 0)

    def normalized_achieved_sec(self):
        """Convert achieved sec into '%H-%M-%S'."""
        m, s = map(int, divmod(self._achieved_sec, 60))
        h, m = map(int, divmod(m, 60))
        return '{:5}h {:2}m {:2}s'.format(h, m, s)
