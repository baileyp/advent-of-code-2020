def part1(file):
    """
    O(n log n) time and O(1) space
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
    """
    O(n log n) time and O(1) space
    :param file:
    :return:
    """
    num_permutations = 1
    for diffs in find_contiguous_1_jolt_diffs(sorted(int(line) for line in file)):
        num_permutations *= min(1 << len(diffs) - 2, 7)
    return num_permutations


def find_contiguous_1_jolt_diffs(jolts):
    contiguous = [0]
    rating = 0
    for jolt in jolts:
        if jolt - rating == 1:
            contiguous.append(jolt)
        else:
            if len(contiguous) > 2:
                yield contiguous
            contiguous = [jolt]
        rating = jolt
    if len(contiguous) > 2:
        yield contiguous

