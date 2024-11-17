from Solver.BasisTransitionSolver import BasisTransitionSolver
from Classes.Vector import Vector
from Classes.Matrix import Matrix

class CoordinateTransitionSolver(BasisTransitionSolver):
    """A class for transition between coordinate systems with known common points
    Args:
        BasisTransitionSolver (Solver): for coordinate transition
    """
    def __init__(self, input_list: list[Matrix | Vector]):
        """calculates key points and transition matrixes
        Args:
            input_list (list[Matrix | Vector]): list, containing the known common point as two matrices
        """
        self._keypointa = Vector(input_list[0].columns()[0])
        self._keypointb = Vector(input_list[1].columns()[0])
        input_x = []
        input_x.append(Matrix(input_list[0].columns()[1:]).transposed())
        input_x.append(Matrix(input_list[1].columns()[1:]).transposed())
        input_x[0] = input_x[0] - Matrix([self._keypointa.tolist()]*input_x[0].cols())
        input_x[1] = input_x[1] - Matrix([self._keypointb.tolist()]*input_x[1].cols())
        super().__init__(input_x)
    
    def set_transition(self, initindex = 0, targetindex = 0):
        """sets the transition matrixes for transpoint and revertpoint"""
        self._keypointa = Vector(self._input[initindex].columns()[0])
        self._keypointb = Vector(self._input[targetindex].columns()[0])
        input_x = []
        input_x.append(Matrix(self._input[initindex].coumns()[1:]).transposed())
        input_x.append(Matrix(self._input[targetindex].columns()[1:]).transposed())
        input_x[0] = input_x[0] - Matrix([self._keypointa.tolist()]*input_x[0].cols())
        input_x[1] = input_x[1] - Matrix([self._keypointb.tolist()]*input_x[1].cols())
        self._input = self._input + input_x
        super().set_transition(-2, -1)
        self._input = self._input[:-2]

    def transpoint(self, vector: Vector | Matrix):
        """transitions given points to target coordinate system"""
        if isinstance(vector, Vector):
            return self._keypointb.tomatrix() + self._transmat*(vector.tomatrix() - self._keypointa)
        key_point_matrix_a = Matrix([self._keypointa.tolist()]*vector.cols()).transposed()
        key_point_matrix_b = Matrix([self._keypointb.tolist()]*vector.cols()).transposed()
        return self._transmat*(vector-key_point_matrix_a)+key_point_matrix_b
    
    def revertpoint(self, vector: Vector | Matrix):
        """transitions the points back to initial coordinate system"""
        if isinstance(vector, Vector):
            return self._keypointa.tomatrix() + self._revmat*(vector.tomatrix()
                                                              -self._keypointb)
        key_point_matrix_a = Matrix([self._keypointa.tolist()]*vector.cols()).transposed()
        key_point_matrix_b = Matrix([self._keypointb.tolist()]*vector.cols()).transposed()
        return self._revmat*(vector-key_point_matrix_b)+key_point_matrix_a
        