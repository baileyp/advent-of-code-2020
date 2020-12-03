# Advent of Code 2020

These are my solutions for the [2020 Advent of Code puzzles](https://adventofcode.com/2020).

## Requirements

 1. Python 3
 
## Setup

None

## Running

Just use `python` to run the `aoc` module.

To run Day 1, Part 1 with the input I received:

```bash
$ python -m aoc 1 1
```

Or you can run it with any input file

```bash
$ python -m aoc 1 1 path/to/input/file.txt
```

Or you can run it with input directly as an argument

```bash
$ python -m aoc 1 1 abcdefg
```

## Notes

Within the comments of each file I'll be capturing some very simple notes about the algorithm and space/time complexity.
In any notes that reference Big O notation, `n` will always refer to the number of lines or items in the puzzle input,
unless otherwise noted.

### Puzzles

Here are my thoughts or lessons learned from the puzzles.

#### Day 1 ([puzzle](https://adventofcode.com/2020/day/1), [solution](./aoc/solution/day01.py))

Nothing crazy with this one - to be expected for the first day. ~~I will note that my solution for part 1 would miss the
edge case of the expense pair being `1010` and `1010` but I figured that was not very likely and wanted to optimize for
**O(1)** lookups of the 2nd value by using `set()`.~~ I came back to this and added an integration test for this
edge case and updated the implementation, which is now definitely in quadratic time. There's a linear time solution here
but I'll leave that as an exercise for another day. Also, because the loop pops items off the set, this algorithm is
technically asymptotic. ~~Either way, is it a bit of a cheat to call this **O(n)** time instead of **O(n^2)**? Maybe ;)~~

For part 2, there might be some trick that avoids cubic time but I had a finite amount of time this morning and, well,
in this case `n` is only 200 so I just went with it. Would love to come back when I have more time and do better.
*UPDATE:* I added an integration test for the edge case where the same value could be used twice (thrice is not valid
since 2020 does not evenly divide into three) and updated the implementation to accomodate it. Still cubic time though.

#### Day 2 ([puzzle](https://adventofcode.com/2020/day/2), [solution](./aoc/solution/day02.py))

I always seem to fall back to regex to parse input like this. I can't always tell if it's the best solution or just a
lazy crutch because I've written gobs of regex in my career and they just come very easily to me. At any rate, input
parsing is not really the point of the challenges these puzzles are all about, but it still must be done.

As to the solutions, I pretty much just went straight for the easiest and most clear implementation. Use Python's
`str.count()` and the native `[]` substring syntax with just a dabble of XOR and that was it.

#### Day 3 ([puzzle](https://adventofcode.com/2020/day/3), [solution](./aoc/solution/day03.py))

Uh, I guess this is just grid traversal? Not too bad. I used some "tricks" in part one to avoid manipulating position
cursors (`deque` ftw) for the "infinite-width" part of this puzzle, but for part 2 it seemed unavoidable due to the need
to reset and walk the grid multiple times.

## Testing

There are both unit tests and integration tests, all of which require `pytest`.

The integration tests prove the full solutions using the sample input data provided by the puzzle descriptions, when
available.

To run:

```bash
# All tests
$ pytest

# Unit Tests
$ pytest tests/unit/

# Integration Tests
$ pytest tests/integration/

```
