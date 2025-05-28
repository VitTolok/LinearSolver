from Solver.Solver import Solver
from Classes.Matrix import Matrix


class LinearSolver(Solver):
    def _linsolve(self, a: int, b: int) -> Matrix:
        """An algorithm that provides a matrix X such that AX=B
        Raises:
            Exception: Matrix A has to be square
            Exception: Matrixes A and B have to have the same number of rows
        Returns:
            Matrix: matrix X
        """
        matrixa = self._input[a]
        matrixb = self._input[b]
        if not isinstance(matrixa, Matrix) or not isinstance(matrixb, Matrix):
            raise Exception
        if not matrixa.is_square():
            raise Exception
        if matrixa.rows() != matrixb.rows():
            raise Exception
        if matrixa.det(True) == complex(0):
            return None
        matrixx = Matrix(
            [[complex(0) for j in range(matrixb.cols())] for i in range(matrixb.rows())]
        )
        for i in range(matrixx.rows()):
            for j in range(matrixx.cols()):
                matrixaij = Matrix(
                    Matrix._transpose(
                        matrixa.columns()[:i]
                        + [matrixb.columns()[j]]
                        + matrixa.columns()[i + 1 :]
                    )
                )
                matrixx.set(i, j, matrixaij.det() / matrixa.det())
        matrixx.det(True)
        return matrixx

    def get_solution(self):
        return self._linsolve(0, 1)
