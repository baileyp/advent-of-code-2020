import pytest
from io import StringIO

from aoc.solution import day01
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('1721, 979, 366, 299, 675, 1456', 514579)
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day01.part1(FileReader(file)) == result
