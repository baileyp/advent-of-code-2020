import pytest
from io import StringIO

from aoc.solution import day11
from aoc.util import FileReader


INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 37),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day11.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ('', None),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day11.part2(FileReader(file)) == result
