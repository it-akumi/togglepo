# coding:utf-8
import json
import os

import click

from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Config
from tglp.goal import Goal
from tglp.span import divide_elapsed_span
from tglp.span import remaining_days


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
    begin = config.get('AGGREGATION_BEGIN')
    time_entries = api.total_time_entries(divide_elapsed_span(begin))

    table = PrettyTable(['Project', 'Goal', 'Achieved', 'Daily Goal', 'Rate'])
    for prj in config.get('PROJECTS'):
        name = prj.get('NAME')
        goal = prj.get('GOAL')
        achieved = time_entries.get(name)
        g = Goal(goal, achieved)
        end = prj.get('END', config.get('END'))
        daily_goal = g.daily_goal(remaining_days(end), config.get('MAX_DAILY_WORKING_HOURS'))
        rate = format(g.achievement_rate(), '.2f')
        table.add_row([name, goal, normalize_second(achieved), normalize_second(daily_goal), rate])

    print(table)


main()
