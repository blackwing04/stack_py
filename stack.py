class Stack:
    def __init__(self, size):
        self._size = size
        self._data_list = [0] * size
        self._top = -1

    def push(self, data):
        if self._top >= self._size - 1:
            return False

        self._top += 1
        self._data_list[self._top] = data
        return True

    def pop(self):
        if self._top <= -1:
            return None

        data = self._data_list[self._top]
        self._top -= 1
        return data
