from Tree_ABC import Tree
import linked_deque

class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def breadthfirst(self):
        if not self.is_empty():
            fringe = linked_deque.LinkedDeque()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
            yield p
            if self.right(p) is not None:
                for other in self._subtree_inorder(self.right(p)):
                    yield other

    def positions(self):
        return self.inorder()