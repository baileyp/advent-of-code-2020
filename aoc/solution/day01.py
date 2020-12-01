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

def part2(file):
    """
    O(n^3) time, O(n) space
    :param file:
    :return:
    """
    expenses = [int(line) for line in file]
    for first in expenses:
        for second in expenses:
            for third in expenses:
                if first + second + third == 2020:
                    return first * second * third

    raise DesignError
