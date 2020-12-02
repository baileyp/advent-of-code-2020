import pytest
from io import StringIO

from aoc.solution import day02
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('1-3 a: abcde, 1-3 b: cdefg, 2-9 c: ccccccccc', 2)
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day02.part1(FileReader(file)) == result
