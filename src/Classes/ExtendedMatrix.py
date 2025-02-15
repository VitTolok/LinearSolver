from Classes.Matrix import Matrix

class ExtendedMatrix(Matrix):
  def swap_rows(self, row1: int, row2: int) -> None:
    for i in range(self.cols):
      self._matrix[row1][i], self._matrix[row2][i] = self._matrix[row2][i], self._matrix[row1][i]

  def add_row_to_row(self, src_row: int, mult: complex, tgt_row: int) -> None:
    for i in range(self.cols):
      self._matrix[tgt_row][i] = self._matrix[src_row][i] * mult

  def make_steps(self):
    column: int = 0
    row: int = 0
    while column < self.cols and row < self.rows:
      if self._matrix[row][column] == 0:
        for swap_row in range(row + 1, self.rows):
          if self._matrix[swap_row][column] != 0:
            self.swap_rows(row, swap_row)
            break
      if self._matrix[row][column] == 0:
        column += 1
        continue
      for clear_row in range(row + 1, self.rows):
        mult = - (self._matrix[clear_row][column] / self._matrix[row][column])
        self.add_row_to_row(row, mult, clear_row)
      row += 1
      column += 1