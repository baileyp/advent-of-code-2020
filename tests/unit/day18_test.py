import pytest

from aoc.solution import day18


@pytest.mark.parametrize('expression, result', [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
])
def test_solve_expression(expression, result):
    assert day18.solve_expression(expression.replace(' ', '')) == result


@pytest.mark.parametrize('expression, start_index, result', [
    ('1 + (2 * 3) + (4 * (5 + 6))', 4, 10),
    ('1 + (2 * 3) + (4 * (5 + 6))', 14, 26),
    ('1 + (2 * 3) + (4 * (5 + 6))', 19, 25),
])
def test_find_balanced(expression, start_index, result):
    assert day18.find_balanced(expression, start_index) == result