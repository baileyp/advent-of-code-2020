import pytest
from unittest import mock
from collections import deque

from aoc.solution import day05


@pytest.mark.parametrize('boarding_pass, row_ins, col_ins, row_col, seat_id', [
    ('BFFFBBFRRR', 'BFFFBBF', 'RRR', [70, 7], 567),
    ('FFFBBBFRRR', 'FFFBBBF', 'RRR', [14, 7], 119),
    ('BBFFBBFRLL', 'BBFFBBF', 'RLL', [102, 4], 820),
])
def test_seat_id(boarding_pass, row_ins, col_ins, row_col, seat_id):
    mock_partition = mock.Mock(side_effect=row_col)
    with mock.patch('aoc.solution.day05.partition', mock_partition):
        assert day05.seat_id(boarding_pass) == seat_id
        mock_partition.assert_has_calls([
            mock.call(list(range(128)), deque(row_ins)),
            mock.call(list(range(8)), deque(col_ins)),
        ])


@pytest.mark.parametrize('values, instructions, result', [
    ([0, 1, 2, 3], ['F', 'B'], 1),
    ([0, 1, 2, 3], ['F', 'F'], 0),
    ([0, 1, 2, 3], ['B', 'B'], 3),
    ([0, 1, 2, 3], ['B', 'F'], 2),
])
def test_partition(values, instructions, result):
    instructions = deque(instructions)

    assert day05.partition(values, instructions) == result
