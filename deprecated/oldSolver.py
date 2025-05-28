# All beyond this point is deprecated////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////
from Classes.Matrix import Matrix
from Classes.Vector import Vector


class oldSolver:
    """A class for calculating algorithms"""

    def __init__(self, matrix1: Matrix | None = None, matrix2: Matrix | None = None):
        """Creates a solver and (optionally) writes down two matrixes
        Args:
            matrix1 (Matrix | None, optional): the first matrix. Defaults to None.
            matrix2 (Matrix | None, optional): the second matrix. Defaults to None.
        """
        self.matrixa = matrix1.copy() if isinstance(matrix1, Matrix) else Matrix([[0]])
        self.matrixb = matrix2.copy() if isinstance(matrix2, Matrix) else Matrix([[0]])

    def getdeta(self) -> complex:
        """
        Returns:
            complex: the determinator of the first stored matrix
        """
        return self.matrixa.det()

    def getdetb(self) -> complex:
        """
        Returns:
            complex: the determinator of the second stored matrix
        """
        return self.matrixb.det()

    def change_matrixa(self, newmatrix: Matrix) -> None:
        """Changes the first stored matrix for a new one
        Args:
            newmatrix (Matrix): the new matrix to store
        """
        self.matrixa = newmatrix.copy()

    def change_matrixb(self, newmatrix: Matrix) -> None:
        """Changes the second stored matrix for a new one
        Args:
            newmatrix (Matrix): the new matrix to store
        """
        self.matrixb = newmatrix.copy()

    def change_vectora(self, newvector: Vector) -> None:
        """changes the first stored vector for a new one
        Args:
            newvector (Vector): the new vector
        """
        self.vectora = newvector.copy()

    def change_vectorb(self, newvector: Vector) -> None:
        """changes the second stored vector for a new one
        Args:
            newvector (Vector): the new vector
        """
        self.vectorb = newvector.copy()

    def getsummat(self) -> Matrix:
        """
        Returns:
            Matrix: the sum of the stored matrixes
        """
        return self.matrixa + self.matrixb

    def getsubmat(self) -> Matrix:
        """
        Returns:
            Matrix: the first stored matrix minus th second one
        """
        return self.matrixa - self.matrixb

    def getmultmat(self) -> Matrix:
        """
        Returns:
            Matrix: the product of the stored matrixes, one of them can also store one number
        """
        if self.matrixb.cols() == self.matrixb.rows() == 1:
            return self.matrixa * self.matrixb.det()
        elif self.matrixa.cols() == self.matrixa.rows() == 1:
            return self.matrixb * self.matrixa.det()
        return self.matrixa * self.matrixb

    def getdivmat(self) -> Matrix:
        """Matrix division by inverted matrix multiplication
        Raises:
            Exception: the divisor must be square
        Returns:
            Matrix: the result of the division
        """
        if not self.matrixb.is_square():
            raise Exception
        e = Matrix(
            [
                [(1 + 0j) if i == j else (0j) for j in range(self.matrixb.cols())]
                for i in range(self.matrixb.cols())
            ]
        )
        tempsolver = oldSolver(self.matrixb, e)
        return self.matrixa * tempsolver.linsolve()

    def linsolve(self) -> Matrix:
        """An algorithm that provides a matrix X such that AX=B
        Raises:
            Exception: Matrix A has to be square
            Exception: Matrixes A and B have to have the same number of rows
        Returns:
            Matrix: matrix X
        """
        if not self.matrixa.is_square():
            raise Exception
        if self.matrixa.rows() != self.matrixb.rows():
            raise Exception
        if self.matrixa.det() == complex(0):
            return None
        matrixx = Matrix(
            [
                [complex(0) for j in range(self.matrixb.cols())]
                for i in range(self.matrixb.rows())
            ]
        )
        for i in range(matrixx.rows()):
            for j in range(matrixx.cols()):
                matrixaij = Matrix(
                    Matrix._transpose(
                        self.matrixa.columns()[:i]
                        + [self.matrixb.columns()[j]]
                        + self.matrixa.columns()[i + 1 :]
                    )
                )
                matrixx.set(i, j, matrixaij.det() / self.matrixa.det())
        matrixx.det(True)
        return matrixx

    def transmat(self) -> Matrix:
        """Calculates the transition Matrix from basis A to basis B
        Returns:
            Matrix: the transition Matrix
        """
        tempsolve = oldSolver(self.matrixb, self.matrixa)
        return tempsolve.linsolve()

    def transvec(self) -> Matrix:
        """transitions vector from basis A coords to basis B coords
        Returns:
            Matrix: one column containing the result
        """
        transmat = self.transmat()
        return transmat * self.vectora.tomatrix()

    def transpoints(self) -> Matrix:
        """Transitions a vector from one coordinate system to another
        based on the common points they have, points are stored in matrixes
        A and B, ther has to be N+1 points for systems of N dimensions
        Returns:
            Matrix: one column containing the resulting vector
        """
        pointsa = list(map(Vector, self.matrixa.columns()))
        pointsb = list(map(Vector, self.matrixb.columns()))
        vectorsa = [pointsa[i + 1] - pointsa[0] for i in range(len(pointsa) - 1)]
        vectorsb = [pointsb[i + 1] - pointsb[0] for i in range(len(pointsb) - 1)]
        tempsolver = oldSolver(
            Matrix([vector.tolist() for vector in vectorsa]).transposed(),
            Matrix([vector.tolist() for vector in vectorsb]).transposed(),
        )
        transmat = tempsolver.linsolve()
        return pointsb[0].tomatrix() + transmat * (self.vectora - pointsa[0]).tomatrix()

    def getscalmult(self):
        e = Matrix.e(len(self.vectora))
        tempsolver = oldSolver(self.vectora.base(), e)
        transmata = tempsolver.transmat()
        self.vectora.tobase(e, transmata)
        tempsolver = oldSolver(self.vectorb.base(), e)
        transmatb = tempsolver.transmat()
        self.vectorb.tobase(e, transmatb)
        return self.vectora.scal_mult(self.vectorb)

    def getvectmult(self) -> Vector:
        base = self.matrixb
        lst = list(map(Vector, self.matrixa.columns()))
        for vector in lst:
            vector = Vector(vector.tolist(), base)
        product = Vector.vect_mult(lst)
        tempsolver = oldSolver(lst[0].base(), base)
        product.tobase(base, tempsolver.transmat())
        return product
