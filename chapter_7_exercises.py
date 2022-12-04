# R-7.1
# Find second to last node in singly linked list

class SL:
    class Node:
        __slots__ = '_element', '_next'
        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._size == 0

    def first(self, e):
        if self.is_empty():
            self._head = self.Node(e, None)
            self._tail = self._head
            self._size += 1
        return self._head

    def add(self, previous, e):
        if self.is_empty():
            return self.first(e)
        newest = self.Node(e, None)
        previous._next = newest
        self._tail = newest
        self._size += 1
        return newest

    def pop(self):
        if self.is_empty():
            raise Exception('I am empty')
        pop_head = self._head
        self._head = self._head._next
        self._size -= 1
        return pop_head

    def __iter__(self):
        cur = self._head._element
        while cur._next != None:
            yield cur._element
            cur = cur._next





