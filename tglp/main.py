# coding:utf-8
import json

import click

from tglp.api import TogglAPI


@click.command()
def main():
    """Entry point of tglp command."""
    with open('tglp/config.json', 'r') as config:
        c = json.load(config)
    api = TogglAPI(c.get('API_TOKEN'), c.get('WORKSPACE_ID'))
    print(api.get_time_entries(c.get('SINCE')))

main()
