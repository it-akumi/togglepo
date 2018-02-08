# coding:utf-8
"""Entry point of Togglepo."""
import click

from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Config
from tglp.project import Project


@click.command()
def main():
    """Togglepo shows how much you achieve your goals."""
    config = Config().config

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
