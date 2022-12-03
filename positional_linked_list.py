"""
Using a doubly linked list as a base, creating a 'public' interface that converts its use to a positional list
or rather a list that can worst case insert, fetch, delete nodes O(1)

I am struggling for a use case and how it becomes useful here, but I am going to try and conceptualize this in terms
of a 'cursor' when parsing a text file. I believe one of the reasons this becomes useful is that it can maintain it's
position relative to what is around it.  Perhaps in the long-long ago, way back in the beginning in order to parse a file
you literally had to read from the beginning each time and seek to the last recorded position.  Where this could be a
costly procedure if the file were long.  Maintaining a relative position according to what is around it would be a
better way in this instance, but I still don't truly grasp how that would be accomplished.
"""

from DoublyLinkedList import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must e proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._nexter is None:
            raise ValueError("pis no longer valid")
        return p._node

    def _make_position(self, node):  # Encapsulates the last used node
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._nexter)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._nexter)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._nexter)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(
            p
        )  # validate shells the encapsulation of Position and allows direct reference
        return self._insert_between(e, original, original._nexter)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


if __name__ == "__main__":
    P = PositionalList()
    N1 = P.add_first(
        "First Entry"
    )  # Here, it automatically passes in the values you want
    # It still returns the 'p' value so you do need to reference it, but it basically stores the relationships
    # That need to be updated when making all of the insert_between/additions/deletions/etc
    # I guess I am starting to understand this.  It allows one to 'cheat' a little.
    # Instead of needing to explicitly outline what the predecessors/successors will be upon each node creation
    P2 = P.add_after(N1, "Second Entry")
    P3 = P.add_after(P2, "Third Entry")
    P4 = P.add_after(P2, "Fourth Entry")
    P5 = P.add_before(
        P2, "Fifth Entry"
    )  #  This doesn't end up saving much, you still have to maintain this reference
    print(P)
    """
    This allows you to utlize the position that is returned and the reference to the orginal node that serves as the
    Positions 'container' that is passed in as an argument.  I am surprised this book didn't elaborate on this a bit
    more considering it is pretty heavy on the abstraction.  
    
    The reason this becomes a sort of game changer is the speed and utility upgrade.  Although it would still be 
    possible to update the doubly linked list, it would definitely be more verbose than this method.  I am talking using
    the additional methods of add after, add before, delete.  You are basically doing everthing by position, which is 
    just an encapsulated reference to the original node instead of being the original node.
    
    I am being cryptic because my understanding is still infantile.  In an effort to be concise and actual take something
    away from this practice, the real value of this positional list is that it is storing for you ONE location that
    you can use automatically as a reference point to add an element before, after, etc.  
    
    If you didn't have this added interface, you could achieve the same thing but you would have to maintain explicit
    reference to the nodes you want to update or add elements between, etc.  It adds automation to list creation in 
    a way.  Where if you were lucky enough to just need to sequentially add values (although why not just use an array)
    then you could do so with this construct
    
    However, I am starting to see the benefit to nodes in general.  Basically, the world is your oyster.  You could
    create some incredibly complex systems with this because you define how the nodes interact with each other and how
    they connect or what they store.  In my head now I am thinking about enzymes splicing and dicing DNA.
    
    A little further analysis of the Position class:
    -The self._container = is actually the reference to the Node object being created.  I believe it is a reference to
    the instance of the LinkedList, which maintains references to the Node objects created in the constructor.  So upon
    each addition, the _make_position is run and stores the instance information and the node information and returns the
    position to be used thereafter
    """
