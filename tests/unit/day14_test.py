import pytest

from aoc.solution import day14

MASK1 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'


@pytest.mark.parametrize('number, mask, result', [
    (11, MASK1, 73),
    (101, MASK1, 101),
    (0, MASK1, 64),
])
def test_apply_mask(number, mask, result):
    assert day14.apply_mask(number, mask) == result


@pytest.mark.parametrize('number, width, result', [
    (2, 2, ['1', '0']),
    (2, 4, ['0', '0', '1', '0']),
    (7, 4, ['0', '1', '1', '1']),
    (8, 4, ['1', '0', '0', '0']),
    (15, 4, ['1', '1', '1', '1']),
])
def test_int_to_bin_list(number, width, result):
    assert day14.int_to_bin_list(number, width) == result
