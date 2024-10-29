from Solver.LinearSolver import LinearSolver
from Classes.Matrix import Matrix
from Classes.Vector import Vector

class BasisTransitionSolver(LinearSolver):
    def __init__(self, input_list: list | None = None):
        super().__init__(input_list)
        self._transmat = self.transmat(0, 1)
        self._revmat = self.transmat(1, 0)
    
    def transmat(self, initindex: int, targetindex: int):
        """Calculates the transition Matrix from basis A to basis B
        Returns:
            Matrix: the transition Matrix
        """
        return self._linsolve(targetindex, initindex)
    
    def transvec(self, vector: Vector | Matrix):
        if isinstance(vector, Vector):
            return Vector((self._transmat * vector.tomatrix()).columns()[0])
        return self._transmat * vector
    
    def revertvec(self, vector: Vector):
        if isinstance(vector, Vector):
            return Vector((self._revmat * vector.tomatrix()).columns()[0])
        return self._revmat * vector
    
    def get_solution(self):
        return self._transmat
