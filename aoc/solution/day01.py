from aoc.exceptions import DesignError


def part1(file):
    """
    O(n) time and space
    :param file:
    :return:
    """
    expenses = set([int(line) for line in file])
    while len(expenses):
        first = expenses.pop()
        second = 2020 - first
        if second in expenses:
            return first * second
    raise DesignError
