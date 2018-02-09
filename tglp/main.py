# coding:utf-8
"""Entry point of Togglepo."""
import click

from prettytable import PrettyTable

import tglp
from tglp.api import TogglAPI
from tglp.config import Config
from tglp.project import Project


@click.option('--conf', default='~/.tglp.json', help='Use specified config.')
@click.version_option(message='Togglepo {}'.format(tglp.__version__))
@click.command()
def main(conf):
    """Togglepo shows how much you achieve your goals."""
    config = Config(conf).config

    api = TogglAPI(
        config.get('API_TOKEN'),
        config.get('WORKSPACE_ID'),
        config.get('AGGREGATION_BEGIN'),
    )
    time_entries = api.total_time_entries()

    table = PrettyTable(['Project', 'Goal', 'Achieved', 'Rate'])
    for prj in config.get('PROJECTS'):
        name = prj.get('NAME')
        goal = prj.get('GOAL')
        p = Project(name, goal)
        p.set_achieved_sec(time_entries)

        table.add_row([
            name,
            str(goal) + 'h',
            p.normalized_achieved_sec(),
            p.get_achievement_rate()
        ])
    print(table)


main()
