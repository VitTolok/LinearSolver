__name__ = "src.Classes.Matrix"

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

def _transpose(matrix: list) -> list:
    """
    Args:
        matrix (list): 2D list containing the elements of the matrix

    Returns:
        list: 2D list representation of the transposed matrix
    """
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))]

def __det(matrix: list) -> float:
    """
    Calculates the determinator of the given matrix recursively
    Args:
        matrix (list): 2D list representation of a square matrix

    Returns:
        float: its determinator
    """
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(matrix[i][0]*(-1)**i
               *__det([row[1:] for row in matrix[:i]+matrix[i+1:]])
               for i in range(len(matrix)))


class Matrix:
    """
    A class for storing and operating Matrixes.
    """
    def __init__(self, array_2d: list):
        """
        Constructs a Matrix from its 2D list representation

        Args:
            array_2d (list): 2D list representation of the matrix

        Raises:
            Exception: the 2D list representation isn't rectangular

        Returns:
            Matrix: the constructed Matrix
        """
        if not _is_rectangular(array_2d):
            raise Exception
        self._matrix = array_2d
        self._rows = len(self._matrix)
        self._cols = len(self._matrix[0])
        self._columns = _transpose(self._matrix)
        self._det = None
        if self._cols == self._rows:
            self._det = __det(array_2d)
        return self

    def _tolist(self) -> list:
        """
        Returns:
            list: the 2D list represetation of this Matrix
        """
        return self._matrix
    
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

    def get(self, row: int, column: int) -> float:
        """Fetches the value from a given position

        Args:
            row (int): the needed row, iterated from 0
            column (int): the needed column, iterated from 0

        Returns:
            float: the needed value
        """
        return self._matrix[row][column]
    
    def set(self, row: int, column: int, value: float) -> None:
        """Changes the value at the given position

        Args:
            row (int): the given row
            column (int): the given column
            value (float): the new value
        """
        self._matrix[row][column] = value

    def transposed(self):
        """
        Returns:
            Matrix: transposed version of this matrix
        """
        return Matrix(self._columns)
    
    def is_square(self) -> bool:
        """
        Returns:
            bool: whether this matrix is square or not
        """
        return True if self._rows == self._cols else False
    
    def det(self, recalculate: bool = False) -> float:
        """Returns the determinator of this Matrix,
        since the determinator is only calculated once
        during construction, optionally recalculates it

        Args:
            recalculate (bool, optional): Whether to recalculate.
                Defaults to False.

        Returns:
            float: the determinator
        """
        if recalculate:
            self._det = __det(self._tolist())
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
        if not (self._cols == other._cols
                and self._rows == other._rows):
            raise Exception
        return Matrix([[self._matrix[i][j] + other._matrix[i][j]
                        for j in range(self._cols)
                        ] for i in range(self._rows)])
    
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
        if not (self._cols == other._cols
                and self._rows == other._rows):
            raise Exception
        return Matrix([[self._matrix[i][j] - other._matrix[i][j]
                        for j in range(self._cols)
                        ] for i in range(self._rows)])
    
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
        if not other is Matrix:
            return Matrix([[self._matrix[i][j] * other
                            for j in range(self._cols)
                            ] for i in range(self._rows)])
        elif self._cols != other._rows:
            raise Exception
        return Matrix([[sum([self._matrix[i][k] * other._matrix[k][j]
                             for k in range(self._cols)])
                             for j in range(other._cols)]
                             for i in range(self._rows)])

    def __iadd__(self, other) -> None:
        """Adds the other matrix to this one

        Args:
            other (Matrix): the other matrix

        Raises:
            Exception: the matrixes aren't of the same size
        """
        if not (self._cols == other._cols
                and self._rows == other._rows):
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
        if not (self._cols == other._cols
                and self._rows == other._rows):
            raise Exception
        for i in range(self._rows):
            for j in range(self._cols):
                self.set(i, j, self.get(i, j) - other.get(i, j))
        
