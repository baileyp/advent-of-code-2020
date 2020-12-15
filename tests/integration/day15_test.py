import pytest
from io import StringIO

from aoc.solution import day15
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('0,3,6', 436),
    ('1,3,2', 1),
    ('2,1,3', 10),
    ('1,2,3', 27),
    ('2,3,1', 78),
    ('3,2,1', 438),
    ('3,1,2', 1836),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day15.part1(FileReader(file)) == result


# No integration tests for part 2
