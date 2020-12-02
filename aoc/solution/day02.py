import re


def part1(file):
    """
    O(n * k) time, O(k) space, where n is the number of passwords and k is the length of the longest password
    :param file:
    :return:
    """
    valid_count = 0
    for line in file:
        letter, min_count, max_count, password = parse_input(line)
        if min_count <= password.count(letter) <= max_count:
            valid_count += 1
    return valid_count


def parse_input(line):
    pattern = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): (.+)$")
    if re.match(pattern, line):
        min_count, max_count, letter, password = pattern.findall(line).pop()
        return letter, int(min_count), int(max_count), password
    raise ValueError("Invalid input format")
