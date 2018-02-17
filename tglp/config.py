# coding:utf-8
"""A handler of config."""
import json
import sys
from pathlib import Path


class Config:
    """A handler of config."""

    def __init__(self, config_file):
        """Load config if it exists."""
        config_file_path = Path(config_file).expanduser()
        if not config_file_path.exists():
            sys.stderr.write('No config found\n')
            sys.exit(1)
        with config_file_path.open() as config:
            self.config = json.load(config)
