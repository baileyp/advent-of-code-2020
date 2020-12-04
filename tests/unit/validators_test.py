import pytest
from aoc.lib import validators


@pytest.mark.parametrize('value, result', [
    ('1978', True),
    ('2002', True),
    ('2003', False),
    ('1920', True),
    ('1919', False),
])
def test_birth_year(value, result):
    assert validators.birth_year(value) is result


@pytest.mark.parametrize('value, result', [
    ('2015', True),
    ('2020', True),
    ('2021', False),
    ('2010', True),
    ('2009', False),
])
def test_issue_year(value, result):
    assert validators.issue_year(value) is result


@pytest.mark.parametrize('value, result', [
    ('2025', True),
    ('2030', True),
    ('2031', False),
    ('2020', True),
    ('2019', False),
])
def test_expiration_year(value, result):
    assert validators.expiration_year(value) is result


@pytest.mark.parametrize('value, result', [
    ('60in', True),
    ('58in', False),
    ('190cm', True),
    ('194cm', False),
    ('190in', False),
    ('77in', False),
    ('190', False),
])
def test_height(value, result):
    assert validators.height(value) is result


@pytest.mark.parametrize('value, result', [
    ('#123abc', True),
    ('#123abz', False),
    ('123abc', False),
])
def test_hair_color(value, result):
    assert validators.hair_color(value) is result


@pytest.mark.parametrize('value, result', [
    ('brn', True),
    ('wat', False),
])
def test_eye_color(value, result):
    assert validators.eye_color(value) is result


@pytest.mark.parametrize('value, result', [
    ('000000001', True),
    ('0123456789', False),
])
def test_passport_id(value, result):
    assert validators.passport_id(value) is result
