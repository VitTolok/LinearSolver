__name__ = "src.main"
__package__ = "src"

from Window import Window
from Solver import Solver

solver = Solver()
win = Window(solver=solver)