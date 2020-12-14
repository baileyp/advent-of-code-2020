from aoc.exceptions import DesignError


def part1(file):
    start_time = int(file.single_line())
    elapsed = 0
    buses = [int(bus_id) for bus_id in file.single_line().split(',') if bus_id != 'x']

    while True:
        for bus_id in buses:
            if (start_time + elapsed) % bus_id == 0:
                return bus_id * elapsed
        elapsed += 1

    raise DesignError


def part2(file):
    return None
