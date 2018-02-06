# coding:utf-8
import click

from prettytable import PrettyTable

from tglp.api import TogglAPI
from tglp.config import Parser
from tglp.period import Period


def normalize_second(seconds):
    """Normalize second to '%H-%M-%S'."""
    m, s = map(int, divmod(seconds, 60))
    h, m = map(int, divmod(m, 60))
    return '{:5}h {:2}m {:3}s'.format(h, m, s)


@click.command()
def main():
    """Togglepo shows how much you achieve your goals."""
    conf = Parser().parse_json_config()
    api = TogglAPI(conf.get('API_TOKEN'), conf.get('WORKSPACE_ID'))
    period = Period(conf.get('SINCE'), conf.get('UNTIL'))

    table = PrettyTable(['Project', 'Achieved'])
    for prj, time_sec in api.total_time_entries(period.divide_passed_period()).items():
        achieved = normalize_second(time_sec)
        table.add_row([prj, achieved])
    print(table)


main()
