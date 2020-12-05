from sys import argv
from importlib import import_module
from io import StringIO
from pathlib import Path
from collections import ChainMap
from time import perf_counter

from aoc.util import FileReader


def run():
    # Defaults
    argv.pop(0)
    defaults = {'day': '1', 'part': '1', 'input': '__default__'}
    cli_args = dict(zip(defaults.keys(), argv))
    args = ChainMap(cli_args, defaults)
    day, part, puzzle_input = args.values()
    input_is_file = True

    # Handle puzzle input
    if '__default__' == puzzle_input:
        puzzle_input = Path(f'./resources/day{day.zfill(2)}.txt')
    else:
        input_is_file = Path(puzzle_input).is_file()

    try:
        solution = import_module(f"aoc.solution.day{day.zfill(2)}")
        puzzle_part = getattr(solution, f"part{part}")

        print("Puzzle Answer: ", end="")
        start = perf_counter()
        if input_is_file:
            with open(puzzle_input, 'r') as file:
                print(puzzle_part(FileReader(file)))
        else:
            print(puzzle_part(FileReader(StringIO(puzzle_input))))
        elapsed = perf_counter() - start
        print(f"Solution computed in {elapsed:0.4f} seconds")
        exit(0)
    except FileNotFoundError:
        print(f"Input file {puzzle_input} not found.")
    except AttributeError:
        print(f"Part {part} not found.")
        exit(1)
    except ModuleNotFoundError:
        print(f"Day {day} not found.")
        exit(1)
