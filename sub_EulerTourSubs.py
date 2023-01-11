import EulerTour
import BinaryEulerTour

class Parenthesizetour(EulerTour.EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(', ', end='')
        print(p.element(), end='')
        if not self.tree().is_leaf(p):
            print(' (', end ='')

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')

class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1

