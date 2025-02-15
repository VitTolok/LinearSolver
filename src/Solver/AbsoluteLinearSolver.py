from Solver.Solver import Solver
from Classes.Matrix import Matrix
from Classes.ExtendedMatrix import ExtendedMatrix

class AbsoluteLinearSolver(Solver):
  def abslinsolve(self):
    matrixa = self._input[0]
    matrixb = self._input[1]
    if matrixb._cols != 1:
      raise Exception
    ext_matrix = ExtendedMatrix(matrixa, matrixb)
    ext_matrix.make_steps()
    if ext_matrix.ranka() != ext_matrix.rankb():
      return None
    valid_cols = []
    column = 0
    row = 0
    while row < ext_matrix.rows() and column < ext_matrix.cols():
      if ext_matrix.get(row, column) == 0:
        row += 1
      else:
        valid_cols.append(column)
        column += 1
    return ans_mat