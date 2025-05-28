from Solver.BasisTransitionSolver import BasisTransitionSolver
from Classes.Matrix import Matrix
from Classes.Vector import Vector


class VectorArithmeticsSolver(BasisTransitionSolver):
    """A Solver for Vector Arithmetics Algorithms
    Args:
        BasisTransitionSolver (Solver): for changing basises
    """

    def __init__(self, input_list: list[Matrix | Vector] = None):
        """Writes inputs and calculates transition matrixes
        if a basis is not given it is replaced by an eye matrix
        of the appropriate size
        Args:
            input_list (list[Matrix  |  Vector], optional): the list of inputs.
            The first element is the basis of the first batch.
            The second element is the first batch of vectors.
            The third is the basis of the second batch.
            The fourth is the second batch.
            Defaults to None.
        Raises:
            Exception: No Inputs
        """
        if input_list == None:
            raise Exception
        if input_list[0] is None and input_list[2] is None:
            if not input_list[1] is None:
                input_list[0] = Matrix.e(len(input_list[1]))
                input_list[2] = Matrix.e(len(input_list[1]))
            elif not input_list[3] is None:
                input_list[0] = Matrix.e(len(input_list[3]))
                input_list[2] = Matrix.e(len(input_list[3]))
            else:
                raise Exception
        elif input_list[0] is None:
            input_list[0] = Matrix.e(len(input_list[2]))
        elif input_list[2] is None:
            input_list[2] = Matrix.e(len(input_list[0]))
        super().__init__([input_list[0], input_list[2]])
        if isinstance(input_list[1], Vector):
            input_list[1] = input_list[1].tomatrix()
        if isinstance(input_list[3], Vector):
            input_list[3] = input_list[3].tomatrix()
        self.__basis_1 = input_list[0]
        self.__batch_1 = input_list[1]
        self.__basis_2 = input_list[2]
        self.__batch_2 = input_list[3]
        self.__basis_1.det(True)
        self.__basis_2.det(True)

    def add(self, basis: 0 | 1 | 2) -> Matrix:
        """Calculates the vector sum
        Args:
            basis (0 | 1 | 2): which basis to covert the answer to.
        Returns:
            Matrix: the resulting batch
        """
        if isinstance(self.__batch_1, Vector):
            self.__batch_1 = self.__batch_1.tomatrix()
        if isinstance(self.__batch_2, Vector):
            self.__batch_2 = self.__batch_2.tomatrix()
        if basis == 0:
            self.__batch_1 = self.__basis_1 * self.__batch_1
            self.__batch_2 = self.__basis_2 * self.__batch_2
        elif basis == 1:
            self.__batch_2 = self.revertvec(self.__batch_2)
        else:
            self.__batch_1 = self.transvec(self.__batch_1)
        return self.__batch_1 + self.__batch_2

    def sub(self, basis: 0 | 1 | 2) -> Matrix:
        """calculates vector subtraction
        Args:
            basis (0 | 1 | 2): which basis to covert the answer to.
        Returns:
            Matrix: the resultin batch of vectors
        """
        if isinstance(self.__batch_1, Vector):
            self.__batch_1 = self.__batch_1.tomatrix()
        if isinstance(self.__batch_2, Vector):
            self.__batch_2 = self.__batch_2.tomatrix()
        if basis == 0:
            self.__batch_1 = self.__basis_1 * self.__batch_1
            self.__batch_2 = self.__basis_2 * self.__batch_2
        elif basis == 1:
            self.__batch_2 = self.revertvec(self.__batch_2)
        else:
            self.__batch_1 = self.transvec(self.__batch_1)
        return self.__batch_1 - self.__batch_2

    def scalmult(self) -> complex:
        """calculates the scalar product of two vectors
        Raises:
            Exception: there have to be exactly 2 vectors in the batches
        Returns:
            complex: the scalar product
        """
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix(
                (self.__basis_1 * self.__batch_1).columns()
                + (self.__basis_2 * self.__batch_2).columns()
            ).transposed()
        if batch.cols() == 2:
            first = Matrix([batch.columns()[0]])
            second = Vector(batch.columns()[1]).tomatrix()
            return (first * second).det()
        raise Exception

    def mixmult(self) -> complex:
        """calculates the mixed product of N N-dimensional vectors
        Raises:
            Exception: not enough or too many vectors given
        Returns:
            complex: the mixed product
        """
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix(
                (self.__basis_1 * self.__batch_1).columns()
                + (self.__basis_2 * self.__batch_2).columns()
            ).transposed()
        if batch.cols() == batch.rows():
            return batch.det()
        raise Exception

    def vectormult(self) -> Vector:
        """calculates the vector product of N-1 N-dimensional vectors
        Raises:
            Exception: not enough or too many vectors
        Returns:
            Vector: the vector product in eye basis
        """
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix(
                (self.__basis_1 * self.__batch_1).columns()
                + (self.__basis_2 * self.__batch_2).columns()
            )
        if batch.rows() == batch.cols() - 1:
            return Vector.vect_mult([Vector(line) for line in batch.tolist()])
        raise Exception
