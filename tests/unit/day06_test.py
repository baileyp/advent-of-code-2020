import pytest

from aoc.solution import day06


@pytest.mark.parametrize('file, group_answers', [
    (['ab', 'bc', '', 'ce'], [{'a', 'b', 'c'}, {'c', 'e'}])
])
def test_group_answers_from_file(file, group_answers):
    assert list(day06.group_answers_from_file(file)) == group_answers
