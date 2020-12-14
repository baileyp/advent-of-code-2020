import pytest

from aoc.solution import day12


@pytest.mark.parametrize('coord, bearing, amount, result', [
    ((0, 0), 'E', 2, (2, 0)),
    ((0, 0), 'S', 2, (0, 2)),
    ((0, 0), 'W', 2, (-2, 0)),
    ((0, 0), 'N', 2, (0, -2)),
])
def test_move(coord, bearing, amount, result):
    assert day12.move(coord, bearing, amount) == result


@pytest.mark.parametrize('point, step, times, result', [
    ((0, 0), (1, 1), 3, (3, 3)),
    ((2, 4), (1, -4), 2, (4, -4)),
])
def test_step_by(point, step, times, result):
    assert day12.step_by(point, step, times) == result


@pytest.mark.parametrize('waypoint, direction, degrees, result', [
    ((2, 4), 'R', 90, (-4, 2)),
    ((2, 4), 'L', 270, (-4, 2)),
    ((2, 4), 'R', 180, (-2, -4)),
    ((2, 4), 'R', 270, (4, -2)),
])
def test_rotate_waypoint(waypoint, direction, degrees, result):
    assert day12.rotate_waypoint(waypoint, direction, degrees) == result


@pytest.mark.parametrize('waypoint, result', [
    ((2, 4), (-4, 2)),
    ((-4, 2), (-2, -4)),
    ((-2, -4), (4, -2)),
    ((4, -2), (2, 4)),
])
def test_rotate_right_90(waypoint, result):
    assert day12.rotate_right_90(waypoint) == result
