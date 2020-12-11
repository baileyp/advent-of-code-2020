OCCUPIED = '#'
EMPTY = 'L'


def part1(file):
    """
    O(w * h) time and space, where w is the width of the floor map and h is the height
    :param file:
    :return:
    """
    floor = [list(line) for line in file]

    width = len(floor[0])
    height = len(floor)

    max_entropy = False

    while not max_entropy:
        generation = [[*row] for row in floor]
        max_entropy = True
        for row in range(0, height):
            for col in range(0, width):
                neighbors = [floor[r][c] for c, r in find_neighbors(row, col, height, width)]
                seat = apply_rules(floor[row][col], count_occupied(neighbors))
                if generation[row][col] != seat:
                    max_entropy = False
                    generation[row][col] = seat
        floor = generation

    return sum(count_occupied(row) for row in floor)


def part2(file):
    """
    O(w * h * (w + h)) time and O(w * h) space where w is the width of the floor map and h is the height
    :param file:
    :return:
    """
    floor = [list(line) for line in file]

    width = len(floor[0])
    height = len(floor)

    max_entropy = False

    while not max_entropy:
        generation = [[*row] for row in floor]
        max_entropy = True
        for row in range(0, height):
            for col in range(0, width):
                seat = apply_rules(floor[row][col], count_visible(row, col, floor, height, width), 5)
                if generation[row][col] != seat:
                    max_entropy = False
                    generation[row][col] = seat
        floor = generation

    return sum(count_occupied(row) for row in floor)


def count_occupied(seats):
    return sum(1 for seat in seats if seat == OCCUPIED)


def apply_rules(value, neighbors_occupied, limit=4):
    if value == EMPTY and neighbors_occupied == 0:
        return OCCUPIED
    if value == OCCUPIED and neighbors_occupied >= limit:
        return EMPTY
    return value


def find_neighbors(row, col, height, width):
    for n_row in range(row - 1, row + 2):
        for n_col in range(col - 1, col + 2):
            col_in_bounds = -1 < n_col < width
            row_in_bounds = -1 < n_row < height
            coord_is_self = col == n_col and row == n_row
            if col_in_bounds and row_in_bounds and not coord_is_self:
                yield n_col, n_row


def count_visible(row, col, floor, height, width):
    steps = (
        lambda r, c: (r - 1, c),
        lambda r, c: (r + 1, c),
        lambda r, c: (r - 1, c + 1),
        lambda r, c: (r + 1, c + 1),
        lambda r, c: (r, c - 1),
        lambda r, c: (r, c + 1),
        lambda r, c: (r - 1, c - 1),
        lambda r, c: (r + 1, c - 1)
    )

    return sum(occupied_visible_on_path(row, col, floor, height, width, step) for step in steps)


def occupied_visible_on_path(row, col, floor, height, width, step):
    row, col = step(row, col)
    while -1 < col < width and -1 < row < height:
        if floor[row][col] == '.':
            row, col = step(row, col)
            continue
        if floor[row][col] == OCCUPIED:
            return True
        break
    return False
