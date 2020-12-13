import pytest

from aoc.solution import day12


@pytest.mark.parametrize('coord, bearing, amount, result', [
    ((0, 0), 'E', 2, [2, 0]),
    ((0, 0), 'S', 2, [0, 2]),
    ((0, 0), 'W', 2, [-2, 0]),
    ((0, 0), 'N', 2, [0, -2]),
])
def test_move(coord, bearing, amount, result):
    assert list(day12.move(coord, bearing, amount)) == result
