import pytest
from io import StringIO

from aoc.solution import day14
from aoc.util import FileReader


INPUT = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 165),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day14.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, None),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day14.part2(FileReader(file)) == result
