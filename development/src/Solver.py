__name__ = "src.Solver"
__package__ = "src"

from Classes.Matrix import Matrix

class Solver:
    def __init__(self, matrix1: Matrix | None = None,
                 matrix2: Matrix | None = None):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
 
    def getdet(self) -> float:
        return self.matrix1.det()
