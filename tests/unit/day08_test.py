import unittest

from aoc.exceptions import InfiniteLoop
from aoc.solution import day08


class TestProgram(unittest.TestCase):
    def test_run_infinite_program(self):
        program = day08.Program([('jmp', 0)])
        with self.assertRaises(InfiniteLoop):
            program.run()

    def test_run_non_infinite_program(self):
        program = day08.Program([('acc', 1)])
        program.run()
        assert program.result() == 1

    def test_acc(self):
        program = day08.Program([])
        program.acc(2)
        assert program.result() == 2
        program.acc(-4)
        assert program.result() == -2

    def test_nop(self):
        program = day08.Program([])
        assert program._pos == 0
        program.nop(0)
        assert program._pos == 1

    def test_jmp(self):
        program = day08.Program([])
        assert program._pos == 0
        program.jmp(4)
        assert program._pos == 4
        program.jmp(-5)
        assert program._pos == -1
