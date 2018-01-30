# coding:utf-8
import json

import click

from api import TogglAPI


@click.command()
def main():
    """Entry point of tglp command."""
    with open('config.json', 'r') as config:
        c = json.load(config)
    api = TogglAPI(c['API_TOKEN'], c['WORKSPACE_ID'])
    api.get_time_entries(c['SINCE'])
