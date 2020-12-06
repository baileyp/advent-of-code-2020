import pytest
from io import StringIO

from aoc.solution import day06
from aoc.util import FileReader


INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""

@pytest.mark.parametrize('test_case, result', [
    (INPUT, 11)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day06.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 6)
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day06.part2(FileReader(file)) == result
