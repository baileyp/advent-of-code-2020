import pytest
from io import StringIO

from aoc.solution import day10
from aoc.util import FileReader

INPUT1 = """16
10
15
5
1
11
7
19
6
12
4"""

INPUT2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


@pytest.mark.parametrize('test_case, result', [
    (INPUT1, 35),
    (INPUT2, 220)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day10.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    (INPUT1, 8),
    (INPUT2, 19208),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day10.part2(FileReader(file)) == result
