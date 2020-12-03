import pytest
from io import StringIO

from aoc.solution import day03
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""", 7)
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day03.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""", 336)
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day03.part2(FileReader(file)) == result
