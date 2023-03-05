class BinaryHeapArray_Practice:
    def __init__(self):
        self.A = []
        self.p = 0

    def _addelement(self, k, v):
        if self.p == 0:
            self.A[self.p] = (k, v)
            self.p += 1
