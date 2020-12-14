from sys import maxsize
from aoc.exceptions import DesignError


def part1(file):
    """
    O(n * i) time and O(n) space where n is the number of buses and i is the number of iterations required
    :param file:
    :return:
    """
    start_time = int(file.single_line())
    elapsed = 0
    buses = [int(bus_id) for bus_id in file.single_line().split(',') if bus_id != 'x']

    while elapsed < maxsize:
        for bus_id in buses:
            if (start_time + elapsed) % bus_id == 0:
                return bus_id * elapsed
        elapsed += 1

    raise DesignError


def part2(file):
    """
    I have no idea what the time complexity is for this, but it's O(n) space
    :param file:
    :return:
    """
    _ = file.single_line()
    departure_schedule = {t: int(bus_id) for t, bus_id in enumerate(file.single_line().split(',')) if bus_id != 'x'}

    elapsed = 0
    align_every = 1
    for offset, bus_id in departure_schedule.items():
        while (elapsed + offset) % bus_id != 0:
            elapsed += align_every
        align_every *= bus_id
    return elapsed
