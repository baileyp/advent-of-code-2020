import pytest
from io import StringIO

from aoc.solution import day12
from aoc.util import FileReader


INPUT = """F10
N3
F7
R90
F11"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 25),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day12.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 286),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day12.part2(FileReader(file)) == result
