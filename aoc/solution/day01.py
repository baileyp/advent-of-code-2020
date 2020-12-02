from aoc.exceptions import DesignError


def part1(file):
    """
    O(n^2) time, O(n) space
    :param file:
    :return:
    """
    expenses = [int(line) for line in file]
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
    for k1, first in enumerate(expenses):
        for k2, second in enumerate(expenses):
            for k3, third in enumerate(expenses):
                if k1 != k2 and k1 != k3 and k2 != k3 and first + second + third == 2020:
                    return first * second * third
    raise DesignError
