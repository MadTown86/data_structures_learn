class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def top(self):
        if self.is_empty():
            raise Exception('Empty Exception')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Exception')
        return self._data.pop()