from itertools import product

ACTIVE = '#'
INACTIVE = '.'
OFFSETS = [c for c in product([-1, 0, 1], repeat=3) if c != (0, 0, 0)]
OFFSETS_4D = [c for c in product([-1, 0, 1], repeat=4) if c != (0, 0, 0, 0)]


def part1(file):
    """
    O(x * y * z) time and O(c) space where x, y, and z are the max axis sizes, and c is the max number of active cubes
    :param file:
    :return:
    """
    grid = set()
    for y, line in enumerate(file):
        for x, cube in enumerate(line):
            if cube == ACTIVE:
                grid.add((x, y, 0))

    for _ in range(6):
        generation = set()
        for x in range_for_axis(grid, 0):
            for y in range_for_axis(grid, 1):
                for z in range_for_axis(grid, 2):
                    num_active = sum(1 for neighbor in neighbors(x, y, z, offsets=OFFSETS) if neighbor in grid)
                    is_active = (x, y, z) in grid

                    if not is_active and num_active == 3:
                        generation.add((x, y, z))
                    elif is_active and num_active in (2, 3):
                        generation.add((x, y, z))
        grid = generation

    return len(grid)


def part2(file):
    """
    O(x * y * z * w) time and O(c) space where x, y, z, and w are the max axis sizes, and c is the max number of active
    cubes
    :param file:
    :return:
    """
    grid = set()
    for y, line in enumerate(file):
        for x, cube in enumerate(line):
            if cube == ACTIVE:
                grid.add((x, y, 0, 0))

    for _ in range(6):
        generation = set()
        for x in range_for_axis(grid, 0):
            for y in range_for_axis(grid, 1):
                for z in range_for_axis(grid, 2):
                    for w in range_for_axis(grid, 3):
                        num_active = sum(1 for neighbor in neighbors(x, y, z, w, offsets=OFFSETS_4D) if neighbor in grid)
                        is_active = (x, y, z, w) in grid

                        if not is_active and num_active == 3:
                            generation.add((x, y, z, w))
                        elif is_active and num_active in (2, 3):
                            generation.add((x, y, z, w))
        grid = generation

    return len(grid)


def neighbors(*coords, offsets):
    for offset in offsets:
        yield tuple(sum(point) for point in zip((coords), offset))


def range_for_axis(grid, axis):
    rng = [cube[axis] for cube in grid]
    return range(min(rng) - 1, max(rng) + 2)
