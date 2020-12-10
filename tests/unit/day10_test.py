import pytest

from aoc.solution import day10


@pytest.mark.parametrize('jolts, diffs', [
    ([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], [[4, 5, 6, 7], [10, 11, 12]]),
    ([1, 2, 3, 4, 7], [[0, 1, 2, 3, 4]])
])
def test_find_contiguous_1_jolt_diffs(jolts, diffs):
    assert list(day10.find_contiguous_1_jolt_diffs(sorted(jolts))) == diffs

