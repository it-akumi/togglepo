# coding:utf-8
import json
import os

import click

from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Config
from tglp.period import Period


def normalize_second(seconds):
    """Normalize second to '%H-%M-%S'."""
    m, s = map(int, divmod(seconds, 60))
    h, m = map(int, divmod(m, 60))
    return '{:5}h {:2}m {:3}s'.format(h, m, s)



@click.command()
def main():
    """Togglepo shows how much you achieve your goals."""
    filename = '.tglp.json'
    config_file_path = os.path.join(
        os.getenv('HOME'),
        filename
    )

    with open(config_file_path, 'r') as raw_config:
        conf = Config(json.load(raw_config))
        config = conf.normalized_config()
    api = TogglAPI(config.get('API_TOKEN'), config.get('WORKSPACE_ID'))
    period = Period(config.get('AGGREGATION_START'), config.get('UNTIL'))

    table = PrettyTable(['Project', 'Achieved'])
    for prj, time_sec in api.total_time_entries(period.divide_passed_period()).items():
        achieved = normalize_second(time_sec)
        table.add_row([prj, achieved])
    print(table)


main()
