# coding:utf-8
import click

from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Parser
from tglp.period import Period


@click.command()
def main():
    """Togglepo shows how much you achieve your goals."""
    conf = Parser().parse_json_config()
    api = TogglAPI(conf.get('API_TOKEN'), conf.get('WORKSPACE_ID'))
    period = Period(conf.get('SINCE'), '2020-01-01')

    table = PrettyTable(['Project', 'Achieved'])
    for prj, time_sec in api.total_time_entries(period.divide_passed_period()).items():
        hours = int(time_sec / 3600)
        minutes = int((time_sec - hours * 3600) / 60)
        seconds = time_sec % 60
        achieved = "{:5}h {:2}m {:3}s".format(hours, minutes, seconds)
        table.add_row([prj, achieved])
    print(table)


main()
