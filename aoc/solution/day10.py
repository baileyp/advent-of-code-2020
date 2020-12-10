def part1(file):
    """
    O(log n) time and O(1) space
    :param file:
    :return:
    """
    ones = 0
    threes = 1
    rating = 0
    for jolt in sorted(int(line) for line in file):
        if jolt - rating == 1:
            ones += 1
        else:
            threes += 1
        rating = jolt

    return ones * threes


def part2(file):
    return None
