# coding:utf-8
"""Entry point of Togglepo."""
import json

import click

from prettytable import PrettyTable

import tglp
from tglp.api import TogglAPI
from tglp.config import Config
from tglp.project import Project


def print_table(project_instances):
    """Print project infomation in tabular format."""
    project_table = PrettyTable(['Project', 'Goal', 'Achieved', 'Rate'])
    for prj in project_instances:
        project_table.add_row([
            prj.name,
            str(prj.goal_h) + 'h',
            prj.normalized_achieved_sec(),
            prj.get_achievement_rate()
        ])
    print(project_table)


def print_json(project_instances):
    """Print project infomation in JSON format."""
    project_json = [
        dict(
            Project=prj.name,
            Goal=str(prj.goal_h) + 'h',
            Achieved=prj.normalized_achieved_sec(),
            Rate=prj.get_achievement_rate()
        ) for prj in project_instances
    ]
    print(json.dumps(project_json))


@click.option('--conf', default='~/.tglp.json', help='Use specified config.')
@click.option('--json', is_flag=True, help='Print in json format.')
@click.version_option(message='Togglepo {}'.format(tglp.__version__))
@click.command()
def main(conf, json):
    """Togglepo shows how much you achieve your goals."""
    config = Config(conf).config

    api = TogglAPI(
        config['API_TOKEN'],
        config['WORKSPACE_ID'],
        config['AGGREGATION_BEGIN'],
    )
    time_entries = api.total_time_entries()

    projects = [
        Project(prj['NAME'], prj['GOAL']) for prj in config['PROJECTS']
    ]
    for project in projects:
        project.set_achieved_sec(time_entries)

    if json:
        print_json(projects)
    else:
        print_table(projects)


main()
