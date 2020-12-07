import pytest
from io import StringIO

from aoc.solution import day07
from aoc.util import FileReader


INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


@pytest.mark.parametrize('test_case, result', [
    (INPUT, 4)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day07.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ('', None)
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day07.part2(FileReader(file)) == result
