import pytest

from aoc.util import FileReader


class TestFileReader:

    def test_iteration(self):
        reader = FileReader(['No Whitespace', '\tWith Whitespace   '])
        assert list(reader) == ['No Whitespace', 'With Whitespace']

    def test_single_line(self):
        reader = FileReader(['\tSingle Line   '])
        assert reader.single_line() == 'Single Line'
