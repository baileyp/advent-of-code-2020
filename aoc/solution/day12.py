from collections import deque


def part1(file):
    """
    O(n) time and O(1) space
    :param file:
    :return:
    """
    bearing = deque('ESWN')
    position = 0, 0

    for instruction in file:
        command, value = instruction[:1], int(instruction[1:])
        if command == 'R':
            bearing.rotate(int(-(value / 90)))
        elif command == 'L':
            bearing.rotate(int(value / 90))
        else:
            position = move(position, bearing[0] if command == 'F' else command, value)

    return sum(abs(distance) for distance in position)


def part2(file):
    return None


def move(pos, bearing, amount):
    x, y = pos
    if bearing == 'E':
        return x + amount, y
    if bearing == 'W':
        return x - amount, y
    if bearing == 'N':
        return x, y - amount
    return x, y + amount
