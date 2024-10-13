__name__ = "src.calc.Solver"
from ..Classes.Matrix import Matrix
from ..GUI.Window import Window

class Solver:
    def __init__(self, matrix1: Matrix | None = None,
                 matrix2: Matrix | None = None):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
 
    def getdet(self) -> float:
        return self.matrix1.det()   
    
    def getexec(self, window: Window):
        def exec() -> None:
            lst = window.getinput().split('\n')
            matrix2d = [list(map(int, line.split())) for line in lst]
            self.matrix1 = Matrix(matrix2d)
            window.writemessage(f"det = {self.getdet()}")

        return exec


