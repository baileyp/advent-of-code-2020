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


@pytest.mark.parametrize('number, mask, result', [
    (42, '000000000000000000000000000000X1001X', list('000000000000000000000000000000X1101X')),
    (26, '00000000000000000000000000000000X0XX', list('00000000000000000000000000000001X0XX')),
])
def test_apply_mask_v2(number, mask, result):
    assert day14.apply_mask_v2(number, mask) == result


@pytest.mark.parametrize('number, width, result', [
    (2, 2, ['1', '0']),
    (2, 4, ['0', '0', '1', '0']),
    (7, 4, ['0', '1', '1', '1']),
    (8, 4, ['1', '0', '0', '0']),
    (15, 4, ['1', '1', '1', '1']),
])
def test_int_to_bin_list(number, width, result):
    assert day14.int_to_bin_list(number, width) == result


@pytest.mark.parametrize('address, mask, result', [
    (42, '000000000000000000000000000000X1001X', [26, 27, 58, 59]),
    (26, '00000000000000000000000000000000X0XX', [16, 17, 18, 19, 24, 25, 26, 27]),
])
def test_addresses_from_mask(address, mask, result):
    assert list(day14.addresses_from_mask(address, mask)) == result
