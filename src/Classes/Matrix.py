from math import *


class Matrix:
    """A class for storing and operating Matrixes."""

    __detcache = dict()

    def clear_detcache():
        """clears the determinator calculation cache"""
        Matrix.__detcache = dict()

    def sizeof_detcache():
        """returns the size of determinator calculation cache"""
        return Matrix.__detcache.__sizeof__()

    def e(size: int):
        return Matrix(
            [[1 if i == j else 0 for j in range(size)] for i in range(size)], True
        )

    def _is_rectangular(matrix: list) -> bool:
        """
        Args:
            matrix (list): A 2D list, containing all the elements of the matrix
        Returns:
            bool: whether or not all rows have the same number of elements
        """
        length = len(matrix[0])
        for row in matrix:
            if len(row) != length:
                return False
        return True

    def read(
        string: str, evaluate: bool = True
    ) -> list[list[complex]] | list[list[str]]:
        """a method for reading matrixes from strings
        Args:
            string (str): matrix in string
            evaluate (bool, optional): whether to evaluate expressions.
                Defaults to True.
        Returns:
            list: matrix in list
        """
        string = string.strip()
        while "\n\n" in string:
            string = string.replace("\n\n", "\n")
        lst = string.split("\n")
        if evaluate:
            j = 1j
            matrix_str = [line.split() for line in lst]
            matrix_2d = [
                [
                    complex(eval(matrix_str[a - 1][b - 1]))
                    for b in range(1, len(matrix_str[a - 1]) + 1)
                ]
                for a in range(1, len(matrix_str) + 1)
            ]
        else:
            matrix_2d = [list(line.split()) for line in lst]
        return matrix_2d

    def _transpose(matrix: list) -> list:
        """
        Args:
            matrix (list): 2D list containing the elements of the matrix
        Returns:
            list: 2D list representation of the transposed matrix
        """
        return [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]

    def __det(matrix: list) -> complex:
        """Calculates the determinator of the given matrix recursively
        caches its answers to reduce calculation time at the cost of lots?
        of memory
        Args:
            matrix (list): 2D list representation of a square matrix
        Returns:
            complex: its determinator
        """
        matrix = tuple(tuple(line) for line in matrix)
        if matrix in Matrix.__detcache.keys():
            return Matrix.__detcache[matrix]
        if len(matrix) == 1:
            return matrix[0][0]
        det = sum(
            matrix[i][0]
            * (-1) ** i
            * Matrix.__det([row[1:] for row in matrix[:i] + matrix[i + 1 :]])
            for i in range(len(matrix))
        )
        Matrix.__detcache.update(dict([(matrix, det)]))
        return det

    def __init__(self, array_2d: list, skip_det=False):
        """Constructs a Matrix from its 2D list representation
        Args:
            array_2d (list): 2D list representation of the matrix
        Raises:
            Exception: the 2D list representation isn't rectangular
        Returns:
            Matrix: the constructed Matrix
        """
        if not Matrix._is_rectangular(array_2d):
            raise Exception
        self._matrix = array_2d.copy()
        self._rows = len(self._matrix)
        self._cols = len(self._matrix[0])
        for line in self._matrix:
            for elem in line:
                elem = complex(elem)
        self._columns = Matrix._transpose(self._matrix)
        self._det = None
        if self._cols == self._rows and not skip_det:
            self._det = Matrix.__det(array_2d)

    def tolist(self) -> list[list[complex]]:
        """
        Returns:
            list: the 2D list represetation of this Matrix
        """
        return self._matrix

    def columns(self) -> list[list[complex]]:
        """
        Returns:
            list: list containing columns of this matrix as lists
        """
        return self._columns

    def rows(self) -> int:
        """
        Returns:
            int: the number of rows in this Matrix
        """
        return self._rows

    def cols(self) -> int:
        """
        Returns:
            int: the number of columns in this Matrix
        """
        return self._cols

    def get(self, row: int, column: int) -> complex:
        """Fetches the value from a given position
        Args:
            row (int): the needed row, iterated from 0
            column (int): the needed column, iterated from 0
        Returns:
            complex: the needed value
        """
        return self._matrix[row][column]

    def set(self, row: int, column: int, value: complex) -> None:
        """Changes the value at the given position
        Args:
            row (int): the given row
            column (int): the given column
            value (complex): the new value
        """
        self._matrix[row][column] = value
        self._columns[column][row] = value

    def transposed(self):
        """
        Returns:
            Matrix: transposed version of this matrix
        """
        return Matrix(self._columns, True)

    def is_square(self) -> bool:
        """
        Returns:
            bool: whether this matrix is square or not
        """
        return True if self._rows == self._cols else False

    def copy(self):
        """
        Returns:
            Matrix: a copy of this matrix
        """
        return Matrix([line.copy() for line in self._matrix], True)

    def det(self, recalculate: bool = False) -> complex | None:
        """Returns the determinator of this Matrix,
        since the determinator is only calculated once
        during construction, optionally recalculates it
        Args:
            recalculate (bool, optional): Whether to recalculate.
                Defaults to False.
        Returns:
            complex: the determinator
            None: its abscence
        """
        if recalculate:
            self._det = Matrix.__det(self.tolist()) if self.is_square() else None
        return self._det

    def __add__(self, other):
        """Matrix addition
        Args:
            other (Matrix): a same-sized matrix
        Raises:
            Exception: the matrixes aren't of the same size
        Returns:
            Matrix: the sum of the two matrixes
        """
        if not (self._cols == other._cols and self._rows == other._rows):
            raise Exception
        return Matrix(
            [
                [self._matrix[i][j] + other._matrix[i][j] for j in range(self._cols)]
                for i in range(self._rows)
            ],
            True,
        )

    def __sub__(self, other):
        """subtracts the second matrix from the first one
        does not change any of them, only returns the result
        Args:
            other (Matrix): the matrix to subtract
        Raises:
            Exception: the matrixes aren't of the same size
        Returns:
            Matrix: the result of the subtraction
        """
        if not (self._cols == other._cols and self._rows == other._rows):
            raise Exception
        return Matrix(
            [
                [self._matrix[i][j] - other._matrix[i][j] for j in range(self._cols)]
                for i in range(self._rows)
            ],
            True,
        )

    def __mul__(self, other):
        """Calculates the product of the two matrixes
        Args:
            other (Matrix): the other matrix
        Raises:
            Exception: the matrixes can't be multiplied
                because of their dimensions
        Returns:
            Matrix: the product
        """
        if not (isinstance(other, Matrix)):
            return Matrix(
                [
                    [self._matrix[i][j] * other for j in range(self._cols)]
                    for i in range(self._rows)
                ],
                True,
            )
        elif self._cols != other._rows:
            raise Exception
        return Matrix(
            [
                [
                    sum(
                        [
                            self._matrix[i][k] * other._matrix[k][j]
                            for k in range(self._cols)
                        ]
                    )
                    for j in range(other._cols)
                ]
                for i in range(self._rows)
            ],
            True,
        )

    def __eq__(self, other) -> bool:
        """Checks if matrixes are the same
        Args:
            other (Matrix): the other matrix
        Returns:
            bool: whether they are the same or not
        """
        if isinstance(other, Matrix):
            if self.cols() == other.cols():
                if self.rows() == other.rows():
                    for i in range(self.rows()):
                        for j in range(self.cols()):
                            if self._matrix[i][j] != other._matrix[i][j]:
                                return False
                    return True
        return False

    def __iadd__(self, other) -> None:
        """Adds the other matrix to this one
        Args:
            other (Matrix): the other matrix
        Raises:
            Exception: the matrixes aren't of the same size
        """
        if not (self._cols == other._cols and self._rows == other._rows):
            raise Exception
        for i in range(self._rows):
            for j in range(self._cols):
                self.set(i, j, self.get(i, j) + other.get(i, j))

    def __isub__(self, other) -> None:
        """Subtracts another matrix from this one
        Args:
            other (Matrix): the other matrix
        Raises:
            Exception: the matrixes aren't of the same size
        """
        if not (self._cols == other._cols and self._rows == other._rows):
            raise Exception
        for i in range(self._rows):
            for j in range(self._cols):
                self.set(i, j, self.get(i, j) - other.get(i, j))

    def print(self) -> str:
        """Rounds the results a bit and returns the matrix
        in printable str format
        Returns:
            str: the string to be printed
        """
        printed = self._matrix.copy()
        for line in printed:
            for i in range(len(line)):
                if isinstance(line[i], complex):
                    line[i] = complex(
                        float(f"{line[i].real:.5e}"), float(f"{line[i].imag:.5e}")
                    )
                    if line[i].imag == 0:
                        line[i] = line[i].real
                if isinstance(line[i], float):
                    if int(line[i]) == line[i]:
                        line[i] = int(line[i])
        return "\n".join([" ".join(map(str, line)) for line in printed])

    def __truediv__(self, other: complex):
        """Matrix division by number
        inverted matrix multiplication only implemented
        through solver
        Args:
            other (complex): the thing to divide self by
        Raises:
            Exception: divisor not complex
        Returns:
            Matrix: the result of the division
        """
        if isinstance(other, complex):
            return self * (1 / other)
        else:
            raise Exception

    def __len__(self) -> int:
        return self._rows
