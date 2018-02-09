# coding:utf-8
"""A handler of config."""
import json
import os
import sys


class Config:
    """A handler of config."""

    def __init__(self, config_file):
        """Load config if it exists."""
        config_file_path = os.path.expanduser(config_file)
        if not os.path.exists(config_file_path):
            sys.stderr.write('No config found\n')
            sys.exit(1)
        with open(config_file_path, 'r') as config:
            self.config = json.load(config)
