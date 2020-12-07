import pytest

from aoc.solution import day07


GRAPH = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': [],
}


@pytest.mark.parametrize('line, bag, contents', [
    ('light red bags contain 1 bright white bag, 2 muted yellow bags.', 'light red', {'bright white': 1, 'muted yellow': 2}),
    ('bright white bags contain 1 shiny gold bag.', 'bright white', {'shiny gold': 1}),
    ('faded blue bags contain no other bags.', 'faded blue', {}),
])
def test_parse_line(line, bag, contents):
    assert day07.parse_line(line) == (bag, contents)


@pytest.mark.parametrize('node, search, paths', [
    ('a', 'd', [['a', 'b'], ['a', 'c']]),
    ('b', 'd', [['b']]),
    ('b', 'c', []),
])
def test_dfs(node, search, paths):
    assert list(day07.dfs(GRAPH, node, search, [node], set())) == paths
