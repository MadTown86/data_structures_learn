from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class Node:
        def __init__(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        def __init__(self, _container, _node):
            super().__init__(_container, _node)

        def element(self):
            return super()._element

        def __ne__(self, other):
            super().__ne__(other)

        def __eq__(self, other):
            super().__eq__(other)

    def __init__(self):
        self._root = None
        self._size = 0

    def _is_leaf(self, p):
        node = self._validate(p)
        return node._left is None and node._right is None

    # Private Methods
    def _validate(self, p):
        if isinstance(p, self.Position):
            raise Exception("Not Valid Position")
        if p._container is not self:
            raise Exception("Does Not Belong to this container")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    # Public Methods

    def add_root(self, e):
        if self._size != 0:
            raise Exception("Not Empty")
        self._root = self.Node(e, None, None, None)
        return self._make_position(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise Exception("Already Have A Left Child")
        newest = self.Node(e, p, None, None)
        node._left = newest
        return self._make_position(newest)


    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise Exception("Already Have A Right Child")
        newest = self.Node(e, p, None, None)
        node._right = newest
        return self._make_position(newest)

    def replace(self, p, e):
        prev = self._validate(p)
        ret = prev._node._element
        prev._node._element = e
        return ret

    def delete(self, p):
        old = self._validate(p)
        if not self._is_leaf(p)
            raise Exception("Two children error")
        old._parent._left = old._left
        return old._left

    def attach(self, p, T1, T2):
        if not self._is_leaf(p):
            raise Exception("Can't combine, p is not a leaf")
        node = self._validate(p)
        node._left, node._right = T1._root, T2._root
        T1._root, T2._root = None, None




