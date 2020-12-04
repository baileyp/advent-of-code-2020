from collections import deque


def part1(file):
    """
    O(n) time and O(n * k) space where n is the number of lines and k is the width of each line
    :param file:
    :return:
    """
    rows = deque(file)
    position = deque(range(len(rows.popleft())))
    trees = 0

    while len(rows):
        line = rows.popleft()
        position.rotate(-3)
        if line[position[0]] == '#':
            trees += 1
    return trees


def part2(file):
    """
    O(n) time and O(n * k) space where n is the number of lines and k is the width of each line
    :param file:
    :return:
    """
    lines = list(file)
    cols = len(lines[0])
    rows = len(lines) - 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_trees = 1

    for slope_x, slope_y in slopes:
        col, row = 0, 0
        trees = 0

        while row < rows:
            col += slope_x
            row += slope_y

            col %= cols

            if (lines[row][col]) == '#':
                trees += 1

        total_trees *= trees

    return total_trees
