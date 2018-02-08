# coding:utf-8
"""A handler of config."""
import json
import os


class Config:
    """A handler of config."""

    def __init__(self, config_file_path='~/.tglp.json'):
        """Load config."""
        with open(os.path.expanduser(config_file_path), 'r') as config:
            self.config = json.load(config)
