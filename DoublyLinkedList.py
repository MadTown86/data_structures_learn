

class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_nexter'

        def __init__(self, element, prev, nexter):
            self._element = element
            self._prev = prev
            self._nexter = nexter

    def __str__(self):
        curr = self._header._nexter
        while True:
            if curr._nexter == None:
                raise StopIteration
            print(str(curr._element))
            curr = curr._nexter


    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._nexter = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._nexter = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._nexter
        predecessor._nexter = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._nexter = node._element = None
        return element


if __name__ == "__main__":
    # I need to remember well how these are made, parsed, etc.
    # Basically, for this abstraction, you have to maintain reference to the nodes in order to have the list maintain
    # functionality.

    """
    Just remember that the easiest way in this instance is to capture the reference to the new node as it is created so
    it can be passed as an argument in the creation of an additional node
    """
    D = _DoublyLinkedBase()
    N1 = D._insert_between('First Value', D._header, D._trailer)
    N2 = D._insert_between('Second Value', N1, D._trailer)
    N3 = D._insert_between('Third Value', N2, D._trailer)
    print(D)

