import tkinter as tk
from GUI.SubGUI import SubGUI
from GUI.Input.MatrixArithmeticsInput import MatrixArithmeticsInput
from Classes.Matrix import Matrix
from Solver.MatrixDivisionSolver import MatrixDivisionSolver

class MatrixArithmeticsGUI(SubGUI):
    def __init__(self, master: tk.Tk, button: tk.Button):
        super().__init__(master, button)
        self.__first_input_buffer = ""
        self.__second_input_buffer = ""
        self.__output_buffer = ""
    
    def activate(self):
        super().activate()
        self.__operator_label = tk.Label(self._master,
                                         text="Enter +, - or * below (or even /)")
        self.__operator_input = tk.Entry(self._master, width=5)
        self.__alt_input_b = tk.Button(self._master, text="Alt Input",
                                       activebackground="green", width=15)
        self.__input = MatrixArithmeticsInput(self._master, self.__alt_input_b)
        self.__output_label = tk.Label(self._master, text="Result:")
        self.__output_text = tk.Text(self._master, height=10, width=30)
        self.__execute_b = tk.Button(self._master, text="Execute",
                                     activebackground="green",
                                     width=15, command=self._calculate)
        self.__input.activate([self.__first_input_buffer, self.__second_input_buffer])
        self.__output_text.insert("1.0", self.__output_buffer)
        self.__operator_label.grid(row=0, column=3)
        self.__operator_input.grid(row=1, column=3)
        self.__execute_b.grid(row=2, column=6)
        self.__alt_input_b.grid(row=0, column=6)
        self.__output_label.grid(row=2, column=3)
        self.__output_text.grid(row=2, column=4)

    def collapse(self):
        if super().collapse():
            self.__first_input_buffer = self.__input.read(0)
            self.__second_input_buffer = self.__input.read(1)
            self.__output_buffer = self.__output_text.get("1.0", "end-1c")
            self.__input.collapse()
            self.__operator_label.destroy()
            self.__operator_input.destroy()
            self.__output_label.destroy()
            self.__output_text.destroy()
            self.__execute_b.destroy()
            self.__alt_input_b.destroy()
    
    def _calculate(self):
        matrixa = Matrix(Matrix.read(self.__input.read(0)))
        matrixb = Matrix(Matrix.read(self.__input.read(1)))
        operation_str = self.__operator_input.get()
        if not (operation_str in ['+', '-', '*', '/']):
            SubGUI._write(self.__output_text, "Invalid input")
            return
        try:
            if operation_str == '+':
                matrix_result = matrixa + matrixb
            elif operation_str == '-':
                matrix_result = matrixa - matrixb
            elif operation_str == '*':
                if matrixa.rows() == matrixa.cols() == 1:
                    matrix_result = matrixb * matrixa.det()
                elif matrixb.rows() == matrixb.cols() == 1:
                    matrix_result = matrixa * matrixb.det()
                else:
                    matrix_result = matrixa * matrixb
            else:
                solver = MatrixDivisionSolver([matrixa, matrixb])
                matrix_result = solver.get_solution()
            SubGUI._write(self.__output_text, matrix_result.print())
        except Exception:
            SubGUI._write(self.__output_text, "Invalid input")