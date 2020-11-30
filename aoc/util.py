class FileReader:
    def __init__(self, f):
        self._file = f

    def __iter__(self):
        return map(lambda x: x.strip(), iter(self._file))

    def single_line(self):
        return next(iter(self))
