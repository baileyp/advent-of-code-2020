from collections import deque


def part1(file):
    rows = deque(file)
    position = deque(range(len(rows.popleft())))
    trees = 0

    while len(rows):
        line = rows.popleft()
        position.rotate(-3)
        if line[position[0]] == '#':
            trees += 1
    return trees


def parse_input(line):
    return None
