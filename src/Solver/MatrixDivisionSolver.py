from Classes.Matrix import Matrix
from Solver.LinearSolver import LinearSolver

class MatrixDivisionSolver(LinearSolver):
    def _matdiv(self, a: int, b: int) -> Matrix:
        """Matrix division by inverted matrix multiplication
        Raises:
            Exception: the divisor must be square
        Returns:
            Matrix: the result of the division
        """
        matrixa = self._input[a]
        matrixb = self._input[b]
        if not isinstance(matrixa, Matrix) or not isinstance(matrixb, Matrix):
            raise Exception
        if not matrixb.is_square():
            raise Exception
        self._input.append(Matrix.e(matrixb.cols()))
        invmatb = self._linsolve(b, -1)
        self._input.pop()
        return matrixa * invmatb
    
    def get_solution(self):
        return self._matdiv(0, 1)