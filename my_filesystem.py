class MyFileSystem:
    class MyFile:
        __slots__ = 'e', '_parent'

        def __init__(self, e, parent):
            self.e = e
            self._parent = parent

    class MyDir:
        __slots__ = '_parent', '_children'

        def __init__(self, parent=None):
            self._parent = parent
            self._children = tuple()

    def __init__(self):
        self._root =


