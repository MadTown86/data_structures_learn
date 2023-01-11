import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """
    An arithmetic expression tree
    """

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.

        In single parameter form, token should be a leaf value, aka a number and the expression tree will have
        that value at an isolated node

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator
        :param token:
        :param left:
        :param right:
        """

        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)

