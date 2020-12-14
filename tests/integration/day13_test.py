import pytest
from io import StringIO

from aoc.solution import day13
from aoc.util import FileReader


INPUT = """939
7,13,x,x,59,x,31,19"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 295),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day13.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 1068781),
    ('\n17,x,13,19', 3417),
    ('\n67,7,59,61', 754018),
    ('\n67,x,7,59,61', 779210),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day13.part2(FileReader(file)) == result
