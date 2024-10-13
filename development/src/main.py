from GUI.Window import Window
from calc.Solver import Solver

solver = Solver()
win = Window()
win.changeexec(solver.getexec(win))
