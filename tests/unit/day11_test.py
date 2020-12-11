import pytest
from unittest import mock

from aoc.solution import day11

FLOOR1 = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""

FLOOR2 = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""


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


def test_count_visible():
    floor = []
    row = 'a'
    col = 'b'
    width = 1
    height = 2

    mock_occupied_visible_on_path = mock.Mock(side_effect=list(range(8)))
    with mock.patch('aoc.solution.day11.occupied_visible_on_path', mock_occupied_visible_on_path):
        assert day11.count_visible(row, col, floor, height, width) == sum(range(8))


@pytest.mark.parametrize('floor, row, col, step, result', [
    (FLOOR1, 0, 3, lambda r, c: (r + 1, c), True),
    (FLOOR1, 1, 3, lambda r, c: (r + 1, c), False),
    (FLOOR1, 4, 3, lambda r, c: (r + 1, c), True),
    (FLOOR1, 3, 2, lambda r, c: (r - 1, c - 1), True),
    (FLOOR1, 3, 2, lambda r, c: (r + 1, c + 1), False),
])
def test_occupied_visible_on_path(floor, row, col, step, result):
    floor = [list(line) for line in floor.split("\n")]

    width = len(floor[0])
    height = len(floor)

    assert day11.occupied_visible_on_path(row, col, floor, height, width, step) == result
