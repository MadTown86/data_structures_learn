class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._f = 0
        self._b = 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise Exception('Empty')
        return (self._f - 1) % len(self._data)

    def back(self):
        if self.is_empty():
            raise Exception('Empty')
        return (self._f + self._size - 1) % len(self._data)

    def dequeue_back(self):
        if self.is_empty():
            raise Exception('Empty')
        ans = self._data[self._b]
        self._data[self._b] = None
        self._b = (self._f + self._size - 1) % len(self._data)
        self._size -= 1
        return ans

    def dequeue_front(self):
        if self.is_empty():
            raise Exception('Empty')
        ans = self._data[self._f]
        self._data[self._f] = None
        self._size -= 1
        return ans

    def enqueue_front(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._f = (self._f - 1) % len(self._data)
        self._data[self._f] = e
        self._size += 1


    def enqueue_back(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._b = (self._f + self._size - 1) % len(self._data)
        self._data[self._b] = e
        self._size += 1


    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._f
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._f = 0


if __name__ == "__main__":
    L = ArrayDeque()
    list1 = [1, 2, 3, 4, 5]
    for x in list1:
        L.enqueue_front(x)

#  I believe [None, None, None, None, None, 5, 4, 3, 2, 1]
    print(L)
    for x in list1[:3]:
        L.enqueue_back(x)

# I believe [5, 4, 3, 2, 1, 1, 2, 3, None, None]
    print(L)
    for x in range(0, 3):
        L.dequeue_front()

# I believe [None, None, None, 2, 1, 1, 2, 3, None, None]
    print(L)
    for x in list1:
        L.enqueue_front(x)

    print(L)
# I believe [3, 2, 1, 2, 1, 1, 2, 3, 5, 4]


