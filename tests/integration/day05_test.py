import pytest
from io import StringIO

from aoc.solution import day05
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day05.part1(FileReader(file)) == result


# No integration test available for part 2!
