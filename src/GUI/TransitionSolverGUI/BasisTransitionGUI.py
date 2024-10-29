import tkinter as tk
from GUI.SubGUI import SubGUI
from Classes.Matrix import Matrix
from Solver.BasisTransitionSolver import BasisTransitionSolver

class BasisTransitionGUI(SubGUI):
    def __init__(self, master, button):
        super().__init__(master, button)
        self.__basis_1_buffer = ""
        self.__batch_buffer = ""
        self.__basis_2_buffer = ""
        self.__output_buffer = ""

    def activate(self):
        super().activate()
        self.__basis_1_input = tk.Text(self._master, height=10, width=30)
        self.__batch_input = tk.Text(self._master, height=10, width=30)
        self.__basis_2_input = tk.Text(self._master, height=10, width=30)
        self.__text_output = tk.Text(self._master, height=10, width=30)
        self.__basis_1_label = tk.Label(self._master, text="First Basis:")
        self.__batch_label = tk.Label(self._master,
                text="Vector in first basis:\n(Nothing for transition matrix)")
        self.__basis_2_label = tk.Label(self._master, text="Second Basis:")
        self.__execute_b = tk.Button(self._master, text="Execute",
                                     command=self._calculate)
        SubGUI._write(self.__basis_1_input, self.__basis_1_buffer)
        SubGUI._write(self.__batch_input, self.__batch_buffer)
        SubGUI._write(self.__basis_2_input, self.__basis_2_buffer)
        SubGUI._write(self.__text_output, self.__output_buffer)
        self.__basis_1_input.grid(row=1, column=2)
        self.__batch_input.grid(row=1, column=3)
        self.__basis_2_input.grid(row=1, column=4)
        self.__text_output.grid(row=2, column=3)
        self.__basis_1_label.grid(row=0, column=2)
        self.__batch_label.grid(row=0, column=3)
        self.__basis_2_label.grid(row=0, column=4)
        self.__execute_b.grid(row=2, column=4)
    
    def collapse(self):
        if super().collapse():
            self.__basis_1_buffer = self.__basis_1_input.get("1.0", "end-1c")
            self.__batch_buffer = self.__batch_input.get("1.0", "end-1c")
            self.__basis_2_buffer = self.__basis_2_input.get("1.0", "end-1c")
            self.__output_buffer = self.__text_output.get("1.0", "end-1c")
            self.__basis_1_input.destroy()
            self.__batch_input.destroy()
            self.__basis_2_input.destroy()
            self.__text_output.destroy()
            self.__basis_1_label.destroy()
            self.__batch_label.destroy()
            self.__basis_2_label.destroy()
            self.__execute_b.destroy()
    
    def _calculate(self):
        try:
            basisa = Matrix(Matrix.read(self.__basis_1_input.get("1.0", "end-1c")))
            batchstr = self.__batch_input.get("1.0", "end-1c").strip()
            if batchstr != "":
                batch = Matrix(Matrix.read(batchstr))
            basisb = Matrix(Matrix.read(self.__basis_2_input.get("1.0", "end-1c")))
            solver = BasisTransitionSolver([basisa, basisb])
            if batchstr != "":
                result = solver.transvec(batch).print()
            else:
                result = solver.get_solution().print()
            SubGUI._write(self.__text_output, result)
        except Exception:
            SubGUI._write(self.__text_output, result)