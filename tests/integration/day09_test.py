import pytest
from io import StringIO

from aoc.solution import day09
from aoc.util import FileReader


INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 127)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day09.part1(FileReader(file), 5) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 62),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day09.part2(FileReader(file), 5) == result
