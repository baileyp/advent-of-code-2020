from collections import deque


def part1(file):
    """
    O(n) time and space
    :param file:
    :return:
    """
    return max(seat_id(boarding_pass) for boarding_pass in file)


def part2(file):
    return None


def seat_id(boarding_pass):
    row = partition(list(range(128)), deque(boarding_pass[:7]))
    col = partition(list(range(8)), deque(boarding_pass[7:]))
    return row * 8 + col


def partition(values, instructions):
    """
    O(log n) time, O(1) space, where n is the number of values
    :param values:
    :param instructions:
    :return:
    """
    if len(instructions) == 0:
        return values.pop()
    instruction = instructions.popleft()
    half = int(len(values) / 2)
    return partition(values[:half] if instruction in ('F', 'L') else values[half:], instructions)
