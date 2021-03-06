import pytest
from io import StringIO

from aoc.solution import day01
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('1721, 979, 366, 299, 675, 1456', 514579),
    ('1010, 5, 1010', 1020100),
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day01.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ('1721, 979, 366, 299, 675, 1456', 241861950),
    ('510, 1000, 220, 800', 1000 * 220 * 800),
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day01.part2(FileReader(file)) == result
