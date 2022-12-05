"""
This is a 'Tree' base class abstraction
"""

class Tree:
    # Abstract base class

    # Nested Position Class
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            return not(self == other)

    # Abstract methods
    def root(self):
        raise NotImplementedError("Must be implmemented by subclass")

    def parent(self, p):
        raise NotImplementedError("Must be implmemented by subclass")

    def children(self, p):
        raise NotImplementedError("Must be implmemented by subclass")

    def __len__(self):
        raise NotImplementedError("Must be implmemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
