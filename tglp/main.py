# coding:utf-8
import json
import os
import sys

import click
from prettytable import PrettyTable

from tglp.api import TogglAPI


def config_path():
    """Get absolute path of config.json."""
    tglp_dir = os.path.dirname(__file__)
    config_path = os.path.join(tglp_dir, './config.json')
    if not os.path.exists(config_path):
        sys.stderr.write('config not found...')
        sys.exit(1)
    return config_path


@click.command()
def main():
    """Entry point of tglp command."""
    with open(config_path(), 'r') as config:
        c = json.load(config)
    api = TogglAPI(c.get('API_TOKEN'), c.get('WORKSPACE_ID'))

    table = PrettyTable(['Project', 'Achieved'])
    for project, time_s in api.all_time_entries(c.get('SINCE')).items():
        hours = time_s // 3600
        minutes = (time_s - hours * 3600) // 60
        seconds = time_s % 60
        achieved = "{:5}h {:2}m {:3}s".format(int(hours), int(minutes), seconds)
        table.add_row([project, achieved])
    print(table)


main()
