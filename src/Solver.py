from Classes.Matrix import Matrix
from Classes.Vector import Vector
import Classes

class Solver:
    def __init__(self, matrix1: Matrix | None = None,
                 matrix2: Matrix | None = None):
        self.matrixa = matrix1
        self.matrixb = matrix2
 
    def getdeta(self) -> complex:
        return self.matrixa.det()
    
    def getdetb(self) -> complex:
        return self.matrixb.det()
    
    def change_matrixa(self, newmatrix: Matrix) -> None:
        self.matrixa = newmatrix
    
    def change_matrixb(self, newmatrix: Matrix) -> None:
        self.matrixb = newmatrix
    
    def change_vectora(self, newvector: Vector) -> None:
        self.vectora = newvector.copy()
    
    def change_vectorb(self, newvector: Vector) -> None:
        self.vectorb = newvector.copy()

    def getsummat(self):
        return self.matrixa + self.matrixb
    
    def getsubmat(self):
        return self.matrixa - self.matrixb
    
    def getmultmat(self):
        if self.matrixb.cols() == self.matrixb.rows() == 1:
            return self.matrixa * self.matrixb.det()
        elif self.matrixa.cols() == self.matrixa.rows() == 1:
            return self.matrixb * self.matrixa.det()
        return self.matrixa * self.matrixb
    
    def getdivmat(self):
        if not self.matrixb.is_square():
            raise Exception
        e = Matrix([[(1+0j) if i == j else (0j)
                      for j in range(self.matrixb.cols())]
                      for i in range(self.matrixb.cols())])
        tempsolver = Solver(self.matrixb, e)
        return self.matrixa * tempsolver.linsolve()
    
    def linsolve(self):
        if not self.matrixa.is_square():
            raise Exception
        if self.matrixa.rows() != self.matrixb.rows():
            raise Exception
        if self.matrixa.det() == complex(0):
            return None
        matrixx = Matrix([[complex(0) for j in range(self.matrixb.cols())]
                          for i in range(self.matrixb.rows())])
        for i in range(matrixx.rows()):
            for j in range(matrixx.cols()):
                matrixaij = Matrix(Matrix._transpose(
                                   self.matrixa.columns()[:i]
                                   + [self.matrixb.columns()[j]]
                                   + self.matrixa.columns()[i+1:]))
                matrixx.set(i, j, matrixaij.det()/self.matrixa.det())
        matrixx.det(True)
        return matrixx
    
    def transmat(self):
        tempsolve = Solver(self.matrixb, self.matrixa)
        return tempsolve.linsolve()
    
    def transvec(self):
        transmat = self.transmat()
        return transmat * self.vectora.tomatrix()
    
    def transpoints(self):
        pointsa = list(map(Vector, self.matrixa.columns()))
        pointsb = list(map(Vector, self.matrixb.columns()))
        vectorsa = [pointsa[i+1] - pointsa[0] for i in range(len(pointsa) - 1)]
        vectorsb = [pointsb[i+1] - pointsb[0] for i in range(len(pointsb) - 1)]
        tempsolver = Solver(Matrix([vector.tolist() for vector in vectorsa]).transposed(),
                            Matrix([vector.tolist() for vector in vectorsb]).transposed())
        transmat = tempsolver.linsolve()
        return pointsb[0].tomatrix() + transmat * (self.vectora - pointsa[0]).tomatrix()

        
