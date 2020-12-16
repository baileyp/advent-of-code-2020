import pytest
from io import StringIO

from aoc.solution import day16
from aoc.util import FileReader


INPUT = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 71),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day16.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ('', None),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day16.part2(FileReader(file)) == result
