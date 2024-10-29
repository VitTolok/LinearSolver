from Solver.BasisTransitionSolver import BasisTransitionSolver
from Classes.Vector import Vector
from Classes.Matrix import Matrix

class CoordinateTransitionSolver(BasisTransitionSolver):
    def __init__(self, input_list):
        self._keypointa = Vector(input_list[0].columns()[0])
        self._keypointb = Vector(input_list[1].columns()[0])
        input_x = []
        input_x.append(Matrix(input_list[0].columns()[1:]).transposed())
        input_x.append(Matrix(input_list[1].columns()[1:]).transposed())
        input_x[0] = input_x[0] - Matrix([self._keypointa.tolist()]*input_x[0].cols())
        input_x[1] = input_x[1] - Matrix([self._keypointb.tolist()]*input_x[1].cols())
        super().__init__(input_x)

    def transpoint(self, vector: Vector | Matrix):
        if isinstance(vector, Vector):
            return self._keypointb.tomatrix() + self._transmat*(vector.tomatrix()
                                                                -self._keypointa)
        key_point_matrix_a = Matrix([self._keypointa.tolist()]*vector.cols()).transposed()
        key_point_matrix_b = Matrix([self._keypointb.tolist()]*vector.cols()).transposed()
        return self._transmat*(vector-key_point_matrix_a)+key_point_matrix_b
    
    def revertpoint(self, vector: Vector | Matrix):
        if isinstance(vector, Vector):
            return self._keypointa.tomatrix() + self._revmat*(vector.tomatrix()
                                                              -self._keypointb)
        key_point_matrix_a = Matrix([self._keypointa.tolist()]*vector.cols()).transposed()
        key_point_matrix_b = Matrix([self._keypointb.tolist()]*vector.cols()).transposed()
        return self._revmat*(vector-key_point_matrix_b)+key_point_matrix_a
    
    def get_solution(self):
        return self._transmat
        