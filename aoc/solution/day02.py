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


def part2(file):
    """
    O(n * k) time, O(k) space, where n is the number of passwords and k is the length of the longest password
    :param file:
    :return:
    """
    valid_count = 0
    for line in file:
        letter, pos_a, pos_b, password = parse_input(line)
        if (password[pos_a - 1] is letter) ^ (password[pos_b - 1] is letter):
            valid_count += 1
    return valid_count


def parse_input(line):
    pattern = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): (.+)$")
    if re.match(pattern, line):
        num_a, num_b, letter, password = pattern.findall(line).pop()
        return letter, int(num_a), int(num_b), password
    raise ValueError("Invalid input format")
