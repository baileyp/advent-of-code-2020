from collections import deque


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


def part2(file):
    return None


def is_valid_sum(num_map, number):
    for num in num_map.keys():
        diff = number - num
        if diff != num and num_map.get(diff):
            return True
    return False
