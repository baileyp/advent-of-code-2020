import pytest
from io import StringIO

from aoc.solution import day04
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""", 2)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day04.part1(FileReader(file)) == result
