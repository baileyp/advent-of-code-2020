import pytest

from aoc.solution import day02


@pytest.mark.parametrize('pattern, matches', [
    ('1-3 a: abcde', ('a', 1, 3, 'abcde')),
    ('1-3 b: cdefg', ('b', 1, 3, 'cdefg')),
    ('2-9 c: ccccccccc', ('c', 2, 9, 'ccccccccc')),
])
def test_parse_input(pattern, matches):
    assert day02.parse_input(pattern) == matches
