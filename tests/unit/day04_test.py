import pytest
from unittest import mock


from aoc.solution import day04


def test_passports_from_file():
    file = ['a', 'b', '', 'c']
    mock_line_to_passport_fields = mock.Mock(side_effect=[{'a': 1}, {'b': 2}, {'c': 3}])
    with mock.patch('aoc.solution.day04.line_to_passport_fields', mock_line_to_passport_fields):
        passports = list(day04.passports_from_file(file))
        mock_line_to_passport_fields.assert_has_calls([mock.call(line) for line in file if line != ''])
        assert passports == [{'a': 1, 'b': 2}, {'c': 3}]


@pytest.mark.parametrize('pattern, fields', [
    ('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd', {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd'
    }),
])
def test_line_to_passport_fields(pattern, fields):
    assert day04.line_to_passport_fields(pattern) == fields


@pytest.mark.parametrize('passport, required, valid', [
    ({'a': 1}, ['a'], True),
    ({'a': 1}, ['a', 'b'], False),
    ({'a': 1, 'c': 3}, ['a', 'b'], False),
    ({'a': 1, 'c': 3, 'b': 2}, ['a', 'b'], True),
])
def test_is_valid(passport, required, valid):
    assert day04.is_valid(passport, required) is valid


@pytest.mark.parametrize('passport, validations, valid', [
    ({'a': 1}, {'a': lambda v: v == 1}, True),
    ({'a': 1}, {'a': lambda v: v == 0}, False),
    ({}, {'a': lambda v: True}, False),
])
def test_is_valid_strict(passport, validations, valid):
    assert day04.is_valid_strict(passport, validations) is valid
