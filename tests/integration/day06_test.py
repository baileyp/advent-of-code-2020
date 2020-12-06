import pytest
from io import StringIO

from aoc.solution import day06
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("""abc

a
b
c

ab
ac

a
a
a
a

b""", 11)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day06.part1(FileReader(file)) == result
