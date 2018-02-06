# coding:utf-8
"""A handler of config."""
import sys


class Config:
    """A handler of config."""

    def __init__(self, config_dict):
        """Set config and error messages of a lack of requirement."""
        self._config = config_dict
        self._required_not_found_errors = dict(
            API_TOKEN='Set Your Toggl API token.\n',
            WORKSPACE_ID='Set workspace id to access.\n',
            AGGREGATION_START='Set start date of data aggregation.\n',
        )

    def _exist_requirements(self):
        """Check if config has all required parameters."""
        for param, error in self._required_not_found_errors.items():
            if self._config.get(param) is None:
                sys.stderr.write('Required parameter not found ')
                sys.stderr.write('in {}.\n'.format(self._config_path))
                sys.stderr.write(error)
                sys.exit(1)

    def normalized_config(self):
        """Return normalized config as dict."""
        self._exist_requirements()
        return self._config
