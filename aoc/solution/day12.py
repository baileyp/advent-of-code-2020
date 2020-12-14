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

    return distance_from_origin(position)


def part2(file):
    """
    O(n) time and O(1) space
    :param file:
    :return:
    """
    position = 0, 0
    waypoint = 10, -1

    for instruction in file:
        command, value = instruction[:1], int(instruction[1:])
        if command in ('R', 'L'):
            waypoint = rotate_waypoint(waypoint, command, value)
        elif command == 'F':
            position = step_by(position, waypoint, value)
        else:
            waypoint = move(waypoint, command, value)

    return distance_from_origin(position)


def distance_from_origin(point):
    return sum(abs(distance) for distance in point)


def move(pos, bearing, amount):
    x, y = pos
    if bearing == 'E':
        return x + amount, y
    if bearing == 'W':
        return x - amount, y
    if bearing == 'N':
        return x, y - amount
    return x, y + amount


def step_by(point, step, times):
    x_delta, y_delta = [times * distance for distance in step]
    x, y = point
    return x + x_delta, y + y_delta


def rotate_waypoint(waypoint, direction, degrees):
    if direction == 'L':
        degrees = 360 - degrees
    for _ in range(int(degrees / 90)):
        waypoint = rotate_right_90(waypoint)

    return waypoint


def rotate_right_90(waypoint):
    x, y = waypoint
    return -y, x
