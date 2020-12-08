import pytest
from io import StringIO

from aoc.solution import day08
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""", 5)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day08.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ('', None),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day08.part2(FileReader(file)) == result
