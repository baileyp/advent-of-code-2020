REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def part1(file):
    """
    O(n) time and O(1) space where n is the number of passports in the input
    :param file:
    :return:
    """
    valid_count = 0
    passport = dict()

    for line in file:
        if line is '':
            if is_valid(passport, REQUIRED_FIELDS):
                valid_count += 1
            passport = dict()
            continue
        passport = {**passport, **line_to_passport_fields(line)}

    if is_valid(passport, REQUIRED_FIELDS):
        valid_count += 1

    return valid_count


def line_to_passport_fields(line):
    parts = map(lambda part: part.split(':'), line.split(' '))
    return {k: v for k, v in parts}


def is_valid(passport, required):
    return all(field in passport for field in required)
