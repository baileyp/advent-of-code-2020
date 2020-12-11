import pytest

from aoc.solution import day11


@pytest.mark.parametrize('row, col, height, width, neighbors', [
    (1, 1, 3, 3, [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]),
    (0, 0, 3, 3, [(1, 0), (0, 1), (1, 1)]),
    (2, 2, 3, 3, [(1, 1), (2, 1), (1, 2)]),
])
def test_find_neighbors(row, col, height, width, neighbors):
    assert list(day11.find_neighbors(row, col, height, width)) == neighbors


@pytest.mark.parametrize('seats, count', [
    ('#.##.#', 4),
    (['#', 'L', '.', '#'], 2),
])
def test_count_occupied(seats, count):
    assert day11.count_occupied(seats) == count


@pytest.mark.parametrize('seat, num, result', [
    (day11.OCCUPIED, 0, day11.OCCUPIED),
    (day11.OCCUPIED, 2, day11.OCCUPIED),
    (day11.OCCUPIED, 4, day11.EMPTY),
    (day11.EMPTY, 0, day11.OCCUPIED),
    (day11.EMPTY, 1, day11.EMPTY),
])
def test_apply_rules(seat, num, result):
    assert day11.apply_rules(seat, num) == result
