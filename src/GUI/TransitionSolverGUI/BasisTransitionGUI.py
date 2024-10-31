import tkinter as tk
from GUI.SubGUI import SubGUI
from GUI.Input.BasisTransitionInput import BasisTransitionInput
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
        self.__alt_input_b = tk.Button(self._master, text="Alt Input",
                                       activebackground="green")
        self.__input = BasisTransitionInput(self._master, self.__alt_input_b)
        self.__text_output = tk.Text(self._master, height=10, width=30)
        self.__basis_1_label = tk.Label(self._master, text="First Basis:")
        self.__batch_label = tk.Label(self._master,
                text="Vector in first basis:\n(Nothing for transition matrix)")
        self.__basis_2_label = tk.Label(self._master, text="Second Basis:")
        self.__result_label = tk.Label(self._master, text="Result:")
        self.__execute_b = tk.Button(self._master, text="Execute",
                                     activebackground="green",
                                     command=self._calculate)
        SubGUI._write(self.__text_output, self.__output_buffer)
        self.__input.activate([self.__basis_1_buffer,
                               self.__batch_buffer,
                               self.__basis_2_buffer])
        self.__alt_input_b.grid(row=0, column=6)
        self.__result_label.grid(row=3, column=2)
        self.__text_output.grid(row=3, column=3)
        self.__basis_1_label.grid(row=0, column=2)
        self.__batch_label.grid(row=0, column=3)
        self.__basis_2_label.grid(row=0, column=5)
        self.__execute_b.grid(row=3, column=5)
    
    def collapse(self):
        if super().collapse():
            self.__basis_1_buffer = self.__input.read(0)
            self.__batch_buffer = self.__input.read(1)
            self.__basis_2_buffer = self.__input.read(2)
            self.__output_buffer = self.__text_output.get("1.0", "end-1c")
            self.__input.collapse()
            self.__alt_input_b.destroy()
            self.__result_label.destroy()
            self.__text_output.destroy()
            self.__basis_1_label.destroy()
            self.__batch_label.destroy()
            self.__basis_2_label.destroy()
            self.__execute_b.destroy()
    
    def _calculate(self):
        try:
            basisa = Matrix(Matrix.read(self.__input.read(0)))
            batchstr = self.__input.read(1).strip()
            if batchstr != "":
                batch = Matrix(Matrix.read(batchstr))
            basisb = Matrix(Matrix.read(self.__input.read(2)))
            solver = BasisTransitionSolver([basisa, basisb])
            if batchstr != "":
                result = solver.transvec(batch).print()
            else:
                result = solver.get_solution().print()
            SubGUI._write(self.__text_output, result)
        except Exception:
            SubGUI._write(self.__text_output, "Invalid Input")