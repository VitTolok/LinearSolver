from Solver.BasisTransitionSolver import BasisTransitionSolver
from Classes.Matrix import Matrix
from Classes.Vector import Vector

class VectorArithmeticsSolver(BasisTransitionSolver):
    def __init__(self, input_list: list[Matrix | Vector] = None):
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
    
    def add(self, basis: 0 | 1 | 2) -> Matrix:
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
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix((self.__basis_1*self.__batch_1).columns() +
                           (self.__basis_2*self.__batch_2).columns()).transposed()
        if batch.cols() == 2:
            first = Matrix([batch.columns()[0]])
            second = Vector(batch.columns()[1]).tomatrix()
            return (first*second).det()
        raise Exception
    
    def mixmult(self) -> complex:
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix((self.__basis_1*self.__batch_1).columns() +
                           (self.__basis_2*self.__batch_2).columns()).transposed()
        if batch.cols() == batch.rows():
            return batch.det()
        raise Exception
    
    def vectormult(self) -> Vector:
        if self.__batch_1 is None and self.__batch_2 is None:
            raise Exception
        elif self.__batch_1 is None:
            batch = self.__basis_2 * self.__batch_2
        elif self.__batch_2 is None:
            batch = self.__basis_1 * self.__batch_1
        else:
            batch = Matrix((self.__basis_1*self.__batch_1).columns() +
                           (self.__basis_2*self.__batch_2).columns())
        if batch.rows() == batch.cols() - 1:
            return Vector.vect_mult([Vector(line) for line in batch.tolist()])
        raise Exception