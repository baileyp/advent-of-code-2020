import pytest

from aoc.solution import day09


@pytest.mark.parametrize('num_map, number, valid', [
    ({1: 1, 2: 2, 3: 3}, 4, True),
    ({1: 1, 2: 2, 3: 3}, 5, True),
    ({1: 1, 2: 2, 3: 3}, 6, False),
])
def test_is_valid_sum(num_map, number, valid):
    assert day09.is_valid_sum(num_map, number) is valid


@pytest.mark.parametrize('numbers, target_sum, result', [
    ([1, 2, 3, 4, 5], 9, [2, 3, 4]),
    ([1, 2, 3, 4, 5], 6, [1, 2, 3]),
    ([1, 2, 3, 4, 5], 7, [3, 4]),
    ([1, 2, 3, 4, 5], 15, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 2, None),
    ([3, 1, 4, 5], 3, None),
    ([3, 1, 2, 4, 5], 3, [1, 2]),
    ([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 127, [15, 25, 47, 40]),
])
def test_find_contiguous_sums_to(numbers, target_sum, result):
    assert day09.find_contiguous_sums_to(numbers, target_sum) == result

