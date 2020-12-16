import re


def part1(file):
    """
    O(n + e) space and O(n + t) time where n is the set of valid ticket values, e is the number of errors, and t is the
    number of tickets
    :param file:
    :return:
    """
    valid = set()
    errors = []

    range_pattern = re.compile(r"^[^:]+: (\d+)-(\d+) or (\d+)-(\d+)$")
    ticket_pattern = re.compile(r"^[\d,]+$")

    for line in file:
        if re.match(range_pattern, line):
            one, two, three, four = (int(num) for num in re.findall(range_pattern, line).pop())
            valid |= set(range(one, two + 1))
            valid |= set(range(three, four + 1))
        elif re.match(ticket_pattern, line):
            ticket = (int(num) for num in line.split(','))
            errors.extend(num for num in ticket if num not in valid)

    return sum(errors)


def part2(file):
    return None

