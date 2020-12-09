import pytest

from aoc.solution import day09


@pytest.mark.parametrize('num_map, number, valid', [
    ({1: 1, 2: 2, 3: 3}, 4, True),
    ({1: 1, 2: 2, 3: 3}, 5, True),
    ({1: 1, 2: 2, 3: 3}, 6, False),
])
def test_is_valid_sum(num_map, number, valid):
    assert day09.is_valid_sum(num_map, number) is valid
