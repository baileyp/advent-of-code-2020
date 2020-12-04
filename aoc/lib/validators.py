import re


def birth_year(year):
    return 1920 <= int(year) <= 2002


def issue_year(year):
    return 2010 <= int(year) <= 2020


def expiration_year(year):
    return 2020 <= int(year) <= 2030


def height(hgt):
    pattern = re.compile(r"^(\d+)(cm|in)$")
    if re.match(pattern, hgt):
        value, unit = pattern.findall(hgt).pop()
        if unit == 'cm':
            return 150 <= int(value) <= 193
        else:
            return 59 <= int(value) <= 76

    return False


def hair_color(color):
    return bool(re.match(r"^#[a-f0-9]{6}$", color))


def eye_color(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def passport_id(pid):
    return bool(re.match(r"^[0-9]{9}$", pid))
