# coding:utf-8
"""Handler of config file."""
import json
import os
import sys


class Parser:
    """A wrapper of JSON parser."""

    def __init__(self, filename='.tglp.json'):
        """Set config file path if it exists."""
        config_file_path = os.path.join(
            os.getenv('HOME'),
            filename
        )

        if os.path.exists(config_file_path):
            self._config_path = config_file_path
        else:
            sys.stderr.write("No config found...\n")
            sys.stderr.write("Is there any config ")
            sys.stderr.write("in your home directory?\n")
            sys.exit(1)

    def parse_json_config(self):
        """Load and return config."""
        with open(self._config_path, 'r') as config_file:
            try:
                config = json.load(config_file)
            except json.decoder.JSONDecodeError:
                sys.stderr.write("Config allowed only ")
                sys.stderr.write("in json format.\n")
                sys.exit(1)
        return config
