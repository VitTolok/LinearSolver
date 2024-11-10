from Solver.LinearSolver import LinearSolver
from Classes.Matrix import Matrix
from Classes.Vector import Vector

class BasisTransitionSolver(LinearSolver):
    """a solver for changing the basis of a batch of vectors
    Args:
        LinearSolver (Solver): for calculating the transition matrix
    """
    def __init__(self, input_list: list | None = None):
        """calculates the forward and backward transition matrixes
        Args:
            input_list (list | None, optional): the input list.
             The first is the basis of the batch.
             The second is the target basis. Defaults to None.
        """
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
        """changes a vectors basis from first to the second"""
        if isinstance(vector, Vector):
            return Vector((self._transmat * vector.tomatrix()).columns()[0])
        return self._transmat * vector
    
    def revertvec(self, vector: Vector):
        """changes a vectors basis from second to the first"""
        if isinstance(vector, Vector):
            return Vector((self._revmat * vector.tomatrix()).columns()[0])
        return self._revmat * vector
    
    def get_solution(self):
        """returns the transition matrix"""
        return self._transmat
