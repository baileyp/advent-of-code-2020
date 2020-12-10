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

#### Day 4 ([puzzle](https://adventofcode.com/2020/day/4), [solution](./aoc/solution/day04.py))

First puzzle where parsing the input is bit more challenging since a single "input" is spread across multiple lines.
Fortunately dictionary merging in Python is pretty easy so no real headache there, although this made me consider
upgrading to 3.9 for dict unions = `a | b` is just so much nicer than `{**a, **b}`.

~~I kind of lament that I had to tag a second "is valid" check at the end of the processing loop but that's just an
artifact of the single-item-across-lines thing. I suppose I could have split the input across double-newlines and
processed it that way, but then that either kills the **O(1)** space or would involve a whole new iterator for reading
files - just didn't seem worth my time.~~ Taking an *excellent* suggestion from a colleague, I moved the passport
creation into a generator - brilliant! Dunno why I didn't think of that - maybe not enough ☕

Part two combined with my goals (decently designed and tested solutions) made for a lot of code, but that's what I set
out to do so, there ya go. Nobody said unit testing was terse. One nice side-effect of this kind of TDD is that once I
have all the code written and all the tests pass, I actually do get the correct puzzle answer on the first try every
time - at least so far ;)

#### Day 5 ([puzzle](https://adventofcode.com/2020/day/5), [solution](./aoc/solution/day05.py))

I was holding my breath for the first puzzle that would demand recursion. Fortunately this is a simple recursive algo,
although I'm convinced there are some sort of "maths" tricks that would maybe make partitioning a list in such a way
just completely irrelevant†. Either way, I went with what I knew and can't complain about **log2** time complexity for
that part.

One thing I tried to look up is how aggregate functions like `max()` perform when a generator is passed. I assumed worst
case in terms of space and thus documented part 1 as needing linear space, but if `max()` updates internally with each
value yielded by the generator, then part 1 would actually be constant space which would be rad if true.

Part 2 of this puzzle is, so far, the only time I couldn't write an integration test to prove the solution. I guess I
technically could have written a unit test for part 2 but that just didn't seem worth my time. Fortunately, running a
diff on sets in Python is pretty simple so I had a high amount of confidence in the result and I did indeed get the
correct answer without any further modifications to the code. Putting on bow on this one and calling it a day.

† Yup - not long after I finished I was reading some other solutions and found what I sort of suspected - the boarding
passes are just obfuscated binary numbers. With that, my `seat_id()` function could be re-written to something like this:

```python
def seat_id(boarding_pass):
    as_binary = boarding_pass\
        .replace('B', '1')\
        .replace('F', '0')\
        .replace('R', '1')\
        .replace('L', '0')
    return int(as_binary, 2)
```

This would completely eliminate the recursion and a lot of unit tests. Still, my solution is my solution so I'm not
going to formally change it, but I did want to make a note here for posterity.

#### Day 6 ([puzzle](https://adventofcode.com/2020/day/6), [solution](./aoc/solution/day06.py))

If there ever was a puzzle designed for the union and intersection of sets, this is it, and that's pretty much all I did
here. Borrowing the [generator technique from day 4](./aoc/solution/day04.py) these puzzles were some of the easiest to
solve so far. Only "trick" I had to do here was for part 2 where the sets had to be initialized with the "full universe"
of answers so that the initial intersection in each group's iteration would succeed.

#### Day 7 ([puzzle](https://adventofcode.com/2020/day/7), [solution](./aoc/solution/day07.py))

I'm not great at graph problems and today was no exception. I knew that I needed to build a graph, which I did as an
adjacency list, and I knew I'd need a DFS function to walk the graph. Also, since the graph is technically a
[DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), I needed to account for multiple paths between two nodes. I
eventually settled on a generator that would yield a path stack every time the target node was found, and then just let
set-uniqueness remove the duplicates.

For part 2 thought it was going to be pretty easy but I kept getting the wrong answers from my integration tests.
Eventually I figured it out and there was a bug in how I was doing the math - I forgot to count the "outer" bags, with
the math looking like this `quantity * inner bag count` instead of `quantity * inner bag count + quantity`. Once that
modification was added everything worked perfectly.

*Note:* Probably the most complex input parsing so far this year.

#### Day 8 ([puzzle](https://adventofcode.com/2020/day/8), [solution](./aoc/solution/day08.py))

Assembler! Ok, I don't love the code I'm pushing for this puzzle. It works, and it performs fine, but it feels clunky
and hacked. The state duplication-as-copies feels janky, forcing the value of the accumulater in part 2 feels **really**
janky, etc. I even skipped some unit tests today because I've been real busy. Will I come back to this and fix it?
Probably not, but maybe. If future puzzles require this program again, I guess I'll likely have to.

I've seen and done these opcode puzzles in previous years so I already had some context and expectations. This is the
first class I've written for AoC this year - whenever I start to see lots of state pile up, I default to OOD - it's
just where my experience is. I think that actually made things complicated for me this time around.

It's also the first day where part 2 introduced enough of a change that I made medium-significant changes to part 1 to 
accommodate - sometimes a sign that the original design was bad, sometimes not. Either way, as lukewarm as I feel about
this code, it does perform really well and produces the right answers so I guess I can't complain about that.

#### Day 9 ([puzzle](https://adventofcode.com/2020/day/9), [solution](./aoc/solution/day09.py))

To me this puzzle feels all about using the right data structures to keep performance tidy. In part 1, I used a map
(`dict()` in Python) for constant-time lookups so that finding a valid sum would be **O(n)** instead of **O(n^2)**, as
well as double-ended queues for managing the working set of numbers in constant time and space as well.

For part 2, I couldn't think of a better solution than just a pair of cursors that walk the list and test sums of the
input numbers between those two cursors until a valid result was found. ~~Early-breaking the loop is key for performance
though - without that this solution takes about 10x longer. So, although it's worst-case an **On(^2)** algorithm, in
application the performance is much better than that.~~ This morning I had somehow convinced myself that a linear-time
algorithm here wouldn't work unless the list was sorted. I honestly don't recall how I got to that conclusion but it
kind of bugged me to push with the performance caveat that I did, so after conferring with some friends I did confirm
that this is possible in linear time *without* sorting, so I updated my solution to reflect. And it *does* perform
better: previous runs took about 0.22 seconds and now it's averaging 0.003 - ~70x faster!

*Side note:* Today is a day where the unit tests really covered me, especially for part 2. I wrote enough tests with
some edge cases that I sorted out some index goofs in my implementation. Once the tests were passing, BOOM, right answer
on the first try.

#### Day 10 ([puzzle](https://adventofcode.com/2020/day/10), [solution](./aoc/solution/day10.py))

As soon as I solved part 1 in basically the time it took to type the code (read: it was *easy*) I knew part 2 would be a
doozy.

It became clear really fast that part 2 was a permutation calculation. At first I had a mild heart attack because I
wasn't sure how I was going to address really large, contiguous sections of 1-diffs and still obey the 3-volt-diff rule.
But then I considered that the challenge might not be that hard so I coded up a quick test and found that no contiguous
section was larger than five. *Excellent*.

From there it was actually remarkably simple. Arrangements are based on whether or not the adapter is present, so just
binary math at that point to get the number of permutations per contiguous group. Only groups of three or more are valid
since the "bookends" of the group cannot be removed, so `2 ^ (group size - 2)` is the math. **However** - when the group
size is five then one of the combinations, all adapters removed, is not valid as it breaks the 3-volt-diff rule - so
those have to be filtered out.

The last "gotcha" was making sure `0` was included in the list so that the correctly-sized contiguous group at the start
of the chain would be generated.

Solutions to both parts required sorting (not sure this is solvable without it) so all the time complexity comes from
that, but I'm really happy that both parts are solvable in **O(1)** space.

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
