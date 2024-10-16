__name__ = "src.Solver"
__package__ = "src"

from Classes.Matrix import Matrix

class Solver:
    def __init__(self, matrix1: Matrix | None = None,
                 matrix2: Matrix | None = None):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
 
    def getdet1(self) -> complex:
        return self.matrix1.det()
    
    def getdet2(self) -> complex:
        return self.matrix2.det()
    
    def change_matrix1(self, newmatrix: Matrix) -> None:
        self.matrix1 = newmatrix
    
    def change_matrix2(self, newmatrix: Matrix) -> None:
        self.matrix2 = newmatrix
    
    def getsum(self):
        return self.matrix1 + self.matrix2
    
    def getsub(self):
        return self.matrix1 - self.matrix2
    
    def getmult(self):
        if self.matrix2.cols() == self.matrix2.rows() == 1:
            return self.matrix1 * self.matrix2.det()
        elif self.matrix1.cols() == self.matrix1.rows() == 1:
            return self.matrix2 * self.matrix1.det()
        return self.matrix1 * self.matrix2
    
    def getdiv(self):
        if self.matrix2.cols() == self.matrix2.rows() == 1:
            return self.matrix1 / self.matrix2.det()
        return self.matrix1 / self.matrix2
