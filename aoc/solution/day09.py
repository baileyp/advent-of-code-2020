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
    O(n) time and space
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
    left, right = 0, 0
    running_sum = 0

    def valid_sum():
        return running_sum == target_sum and right - left > 1

    while right < len(numbers):
        running_sum += numbers[right]
        right += 1

        if valid_sum():
            return numbers[left:right]

        while running_sum > target_sum:
            running_sum -= numbers[left]
            left += 1

            if valid_sum():
                return numbers[left:right]
    return None


def is_valid_sum(num_map, number):
    for num in num_map.keys():
        diff = number - num
        if diff != num and num_map.get(diff):
            return True
    return False
