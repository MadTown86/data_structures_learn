import EulerTour

class PreorderPrintIndentedTour(EulerTour.EulerTour):
    def _hook_previsit(selfself, p, d, path):
        print(2*d*' ' + str(p.element()))