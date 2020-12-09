from collections import deque

from aoc.exceptions import DesignError


def part1(file, preamble_size=25):
    """
    O(n) time and space
    :param file:
    :param preamble_size:
    :return:
    """
    numbers = [int(line) for line in file]
    working_set = deque(numbers[:preamble_size])
    available = deque(numbers[preamble_size:])

    test = available.popleft()
    while is_valid_sum({n: n for n in working_set}, test):
        working_set.popleft()
        working_set.append(test)
        test = available.popleft()

    return test


def part2(file, preamble_size=25):
    """
    O(n^2) time and O(n) space
    :param file:
    :param preamble_size:
    :return:
    """
    numbers = [int(line) for line in file]
    target_sum = part1(numbers, preamble_size)

    contiguous = find_contiguous_sums_to(numbers, target_sum)
    if contiguous:
        return min(contiguous) + max(contiguous)

    raise DesignError


def find_contiguous_sums_to(numbers, target_sum):
    for l in range(len(numbers) - 2):
        for r in range(l + 2, len(numbers) + 1):
            contiguous = numbers[l:r]
            contiguous_sum = sum(contiguous)
            if contiguous_sum == target_sum:
                return contiguous
            if contiguous_sum > target_sum:
                break
    return None


def is_valid_sum(num_map, number):
    for num in num_map.keys():
        diff = number - num
        if diff != num and num_map.get(diff):
            return True
    return False
