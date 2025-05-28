from Classes.Matrix import Matrix


class ExtendedMatrix(Matrix):

    def __init__(self, matrixa: Matrix, matrixb: Matrix):
        self.sep = matrixa._cols
        if matrixa._rows != matrixb._rows:
            raise Exception
        self._matrix = [
            matrixa._matrix[i] + matrixb._matrix[i] for i in range(matrixa._rows)
        ]
        self._rows = matrixa._rows
        self._cols = matrixa._cols + matrixb._cols
        self._columns = Matrix._transpose(self._matrix)
        self._det = None

    def swap_rows(self, row1: int, row2: int) -> None:
        for i in range(self._cols):
            self._matrix[row1][i], self._matrix[row2][i] = (
                self._matrix[row2][i],
                self._matrix[row1][i],
            )

    def add_row_to_row(self, src_row: int, mult: complex, tgt_row: int) -> None:
        for i in range(self._cols):
            self._matrix[tgt_row][i] = self._matrix[src_row][i] * mult

    def mult_row(self, row: int, mult: complex):
        for i in range(self._cols):
            self._matrix[row][i] *= mult

    def make_steps(self):
        column: int = 0
        row: int = 0
        while column < self._cols and row < self._rows:
            if self._matrix[row][column] == 0:
                for swap_row in range(row + 1, self.rows):
                    if self._matrix[swap_row][column] != 0:
                        self.swap_rows(row, swap_row)
                        break
            if self._matrix[row][column] == 0:
                column += 1
                continue
            for clear_row in range(self.rows):
                if clear_row == row:
                    continue
                mult = -(self._matrix[clear_row][column] / self._matrix[row][column])
                self.add_row_to_row(row, mult, clear_row)
            self.mult_row(row, 1 / self._matrix[row][column])
            row += 1
            column += 1

    def ranka(self) -> int:
        rank: int = 0
        for row in range(self._rows):
            for column in range(self.sep):
                if self._matrix[row][column] != 0:
                    rank += 1
                    break
        return rank

    def rankb(self) -> int:
        rank: int = 0
        for row in range(self._rows):
            for column in range(self._cols):
                if self._matrix[row][column] != 0:
                    rank += 1
                    break
        return rank
