from aoc.exceptions import DesignError, InfiniteLoop


def part1(file):
    """
    O(n + l) time and O(n) space, where n in the number of instructions and l is the length of the program before the
    infinite loop is detected
    :param file:
    :return:
    """
    program = Program(file_to_instructions(file))
    try:
        program.run()
    except InfiniteLoop:
        return program.result()

    raise DesignError


def part2(file):
    """
    O(n + r) time and O(n) space, where n is the number of instructions and t is the number of replacement attempts
    :param file:
    :return:
    """
    program = SelfRepairingProgram(file_to_instructions(file))
    program.run()
    return program.result()


def file_to_instructions(file):
    return [(op, int(value)) for op, value in (line.split(' ') for line in file)]


class Program:
    def __init__(self, instructions, visited=None, acc=0, pos=0):
        self._instructions = instructions
        self._visited = visited or set()
        self._acc = acc
        self._pos = pos

    def run(self):
        while self._pos not in self._visited:
            op, value = self._instructions[self._pos]
            self._visited.add(self._pos)
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

    def state(self):
        return {
            'instructions': [*self._instructions],
            'visited': {*self._visited},
            'acc': self._acc + 0,
            'pos': self._pos + 0,
        }


class SelfRepairingProgram(Program):
    def run(self):
        while self._pos < len(self._instructions):
            op, value = self._instructions[self._pos]
            if op in ['nop', 'jmp']:
                result = self._test_repair('jmp' if op == 'nop' else 'nop', value)
                if result:
                    # Hack? If a non-looping result was found, shove it into the accumulator of the program and bail
                    self._acc = result
                    break
            self._visited.add(self._pos)
            getattr(self, op)(value)
        return

    def _test_repair(self, new_op, value):
        test_state = self.state()
        test_state['instructions'][self._pos] = (new_op, value)
        test_program = Program(**test_state)

        try:
            test_program.run()
        except InfiniteLoop:
            return None

        # This program succeeded, send it back to the caller
        return test_program.result()
