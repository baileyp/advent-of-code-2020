import re


def part1(file):
    """
    O(n) time and space
    :param file:
    :return:
    """
    graph = {bag: contents.keys() for bag, contents in (parse_line(line) for line in file)}

    colors = set()
    for node in graph.keys():
        for path in dfs(graph, node, 'shiny gold', [node], set()):
            colors |= set(path)

    return len(colors)


def part2(file):
    return None


def dfs(graph, node, search, path, visited):
    if node not in visited:
        visited.add(node)
        for child in graph[node]:
            if child == search:
                yield path
            yield from dfs(graph, child, search, [*path, child], visited)


def parse_line(line):
    pattern = re.compile(r"^(\d+) (.+?) bags?$")
    bag, contents = line.strip('.').split(' bags contain ')
    if contents == 'no other bags':
        return bag, {}
    return bag, {k: int(v) for v, k in (pattern.findall(item).pop() for item in contents.split(', '))}
