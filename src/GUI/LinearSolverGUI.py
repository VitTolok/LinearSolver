import tkinter as tk
from Classes.Matrix import Matrix
from GUI.SubGUI import SubGUI
from GUI.Input.LinearSolverInput import LinearSolverInput
from Solver.LinearSolver import LinearSolver

class LinearSolverGUI(SubGUI):
    def __init__(self, master: tk.Tk, button: tk.Button):
        super().__init__(master, button)
        self.__matrix_a_buffer = ""
        self.__var_names_buffer = ""
        self.__matrix_b_buffer = ""
        self.__output_buffer = ""
    
    def activate(self):
        super().activate()
        self.__matrix_a_label = tk.Label(self._master, text="Input Multiplicators")
        self.__var_names_label = tk.Label(self._master, text="Variable Names, Vertically")
        self.__alt_input_b = tk.Button(self._master, text="Alt Input",
                                       activebackground="green")
        self.__input = LinearSolverInput(self._master, self.__alt_input_b)
        self.__output_label = tk.Label(self._master, text="Output")
        self.__output_text = tk.Text(self._master, height=10, width=30)
        self.__execute_b = tk.Button(self._master, text="Execute",
                                   activebackground="green",
                                   command=self._calculate)
        SubGUI._write(self.__output_text, self.__output_buffer)
        self.__input.activate([self.__matrix_a_buffer, self.__var_names_buffer,
                               self.__matrix_b_buffer])
        self.__alt_input_b.grid(row=0, column=5)
        self.__matrix_a_label.grid(row=0, column=1)
        self.__var_names_label.grid(row=0, column=2)
        self.__output_label.grid(row=2, column=1)
        self.__output_text.grid(row=2, column=2)
        self.__execute_b.grid(row=2, column=3)
    
    def collapse(self):
        if super().collapse():
            self.__matrix_a_buffer = self.__input.read(0)
            self.__var_names_buffer = self.__input.read(1)
            self.__matrix_b_buffer = self.__input.read(2)
            self.__output_buffer = self.__output_text.get("1.0", "end-1c")
            self.__input.collapse()
            self.__matrix_a_label.destroy()
            self.__var_names_label.destroy()
            self.__output_label.destroy()
            self.__output_text.destroy()
            self.__execute_b.destroy()
            self.__alt_input_b.destroy()
    
    def _calculate(self):
        try:
            matrix_a = Matrix(Matrix.read(self.__input.read(0)))
            var_names_str = self.__input.read(1).strip()
            if var_names_str != "":
                var_names = Matrix.read(var_names_str, False)
            matrix_b = Matrix(Matrix.read(self.__input.read(2)))
            solver = LinearSolver([matrix_a, matrix_b])
            solution = solver.get_solution()
            if var_names_str != "":
                solution = Matrix.read(solution.print(), False)
                result = '\n'.join([' '.join([f"{var_names[i][j]} = {solution[i][j]}"
                                          for j in range(len(solution[0]))])
                                          for i in range(len(solution))])
                SubGUI._write(self.__output_text, result)
            else:
                SubGUI._write(self.__output_text, solution.print())
        except Exception:
            SubGUI._write(self.__output_text, "Invalid input")