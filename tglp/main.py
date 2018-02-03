# coding:utf-8
import click
from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Parser


@click.command()
def main():
    """Togglepo shows how much you achieve your goals."""
    c = Parser().parse_json_config()
    api = TogglAPI(c.get('API_TOKEN'), c.get('WORKSPACE_ID'))

    table = PrettyTable(['Project', 'Achieved'])
    for project, time_s in api.all_time_entries(c.get('SINCE')).items():
        hours = int(time_s / 3600)
        minutes = int((time_s - hours * 3600) / 60)
        seconds = time_s % 60
        achieved = "{:5}h {:2}m {:3}s".format(hours, minutes, seconds)
        table.add_row([project, achieved])
    print(table)


main()
