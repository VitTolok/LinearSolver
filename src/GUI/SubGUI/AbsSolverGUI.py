import tkinter as tk
from Classes.Matrix import Matrix
from GUI.SubGUI.SubGUI import SubGUI
from GUI.SubGUI.LinearSolverGUI import LinearSolverGUI
from Solver.AbsoluteLinearSolver import AbsoluteLinearSolver


class AbsSolverGUI(LinearSolverGUI):
    def _calculate(self):
        try:
            matrix_a = Matrix(Matrix.read(self._input.read(0)))
            var_names_str = self._input.read(1).strip()
            if var_names_str != "":
                var_names = Matrix.read(var_names_str, False)
            else:
                var_names = [[f"x{i}"] for i in range(matrix_a.cols())]
            matrix_b = Matrix(Matrix.read(self._input.read(2)))
            solver = AbsoluteLinearSolver([matrix_a, matrix_b])
            solution = solver.abslinsolve()
            if solution is None:
                SubGUI._write(self._output_text, "No Solutions")
                return

        except Exception:
            SubGUI._write(self.__output_text, "Invalid input")
