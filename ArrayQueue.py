class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._f = 0
        # self._b = 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def front(self):
        if self.is_empty():
            raise Exception('Empty')
        else:
            return self._data[self._f]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty')
        answer = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._f + self._size) % len(self._data)  # The append function for a circular array,
        # HA remember, if you do 8 % 10 - the returned value is 8 because the entire shabang is a remainder
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._f
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)  # I need to try to remember this concept - circular stepwise alteration
        self._f = 0

if __name__ == "__main__":
    L = ArrayQueue()
    # Add 8
    list1 = [1, 5, 10, 33, 10, 5, 2, 3]
    for x in list1:
        L.enqueue(x)

    # del 4
    for x in range(0, 4):
        L.dequeue()

    list2 = [5, 6, 7, 4]
    for x in list2:
        L.enqueue(x)

    print(L)

    # I think the front is going to be index 4 - then it should be [7, 4, None, None, 10, 5, 2, 3, 5, 6]
