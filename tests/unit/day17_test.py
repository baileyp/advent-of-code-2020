import pytest

from aoc.solution import day17


GRID1 = set([
    (0, 2, 1),
    (-5, 0, 10),
    (6, 1, 4),
])

GRID2 = set([
    (0, 0, 1),
    (-5, 0, 10),
    (6, 0, 4),
])

@pytest.mark.parametrize('grid, axis, result', [
    (GRID1, 0, range(-6, 8)),
    (GRID1, 1, range(-1, 4)),
    (GRID1, 2, range(0, 12)),
    (GRID2, 1, range(-1, 2)),
])
def test_range_for_axis(grid, axis, result):
    assert day17.range_for_axis(grid, axis) == result

