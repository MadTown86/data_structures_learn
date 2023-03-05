class PriorityQueueBase:
    """
    Abstract base class for priority queue
    """
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key # Key holds priority

    def is_empty(self):
        return len(self) == 0
    