from aoc.exceptions import DesignError, InfiniteLoop


def part1(file):
    """
    O(n + l) time and O(n) space, where n in the number of instructions and l is the length of the program before the
    infinite loop is detected
    :param file:
    :return:
    """
    program = file_to_program(file)
    try:
        program.run()
    except InfiniteLoop:
        return program.result()

    raise DesignError


def part2(file):
    return None


def file_to_program(file):
    return Program([(op, int(value)) for op, value in (line.split(' ') for line in file)])


class Program:
    def __init__(self, instructions):
        self._instructions = instructions
        self._acc = 0
        self._pos = 0

    def run(self):
        while self._instructions[self._pos] is not None:
            op, value = self._instructions[self._pos]
            self._instructions[self._pos] = None
            getattr(self, op)(value)
            if self._pos >= len(self._instructions):
                return
        raise InfiniteLoop

    def result(self):
        return self._acc

    def acc(self, value):
        self._acc += value
        self._pos += 1

    def nop(self, _):
        self._pos += 1

    def jmp(self, value):
        self._pos += value
