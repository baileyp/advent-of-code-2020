import pytest
from io import StringIO

from aoc.solution import day17
from aoc.util import FileReader


INPUT = """.#.
..#
###"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 112),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day17.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, None),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day17.part2(FileReader(file)) == result
