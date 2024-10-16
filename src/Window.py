__name__ = "src.Window"
__package__ = "src"

import tkinter as tk
from Solver import Solver
from Classes.Matrix import Matrix

class Window:
    
    def __init__(self, solver: Solver):
        self.__noinit()
        self.solver = solver
        self.window = tk.Tk(screenName="LinearSolver",
                                 baseName="LinSol",
                                 className="LinearSolverV0_1")
        self.init_det_b = tk.Button(self.window, text="determinator",
                                    command=self.init_det)
        self.init_det_b.grid(row=0, column=0)
        self.init_ari_b = tk.Button(self.window, text="matrix arithmetics",
                                    command=self.init_ari)
        self.init_ari_b.grid(row=1, column=0)
        self.init_linsolve_b = tk.Button(self.window, text="Linear Equations",
                                        command=self.init_linsolve)
        self.init_linsolve_b.grid(row=2, column=0)
        self.window.mainloop()
    
    def __noinit(self):
        self.det_is_init = False
        self.ari_is_init = False
        self.linsolve_is_init = False
    
    def kys(self):
        self.deinit_det()
        self.deinit_ari()
        self.deinit_linsolve()

    def write(output: tk.Text, text: str) -> None:
            output.delete("1.0", "end-1c")
            output.insert("1.0", text)

    def execdet(self):
        matrix_2d = Matrix.read(self.text_input.get("1.0", "end-1c"))
        try:
            self.solver.change_matrixa(Matrix(matrix_2d))
            det = self.solver.getdeta()
            if isinstance(det, complex):
                det = complex(round(det.real, 4), round(det.imag, 4))
                if det.imag == 0:
                    det = det.real
            if isinstance(det, float):
                if int(det) == det:
                    det = int(det)
            self.answer_message.config(text=f"det = {det}")
        except Exception:
            self.answer_message.config(text="Invalid Input")
    

    def init_det(self):
        self.kys()
        self.det_is_init = True
        self.input_label = tk.Label(self.window, text="Input square matrix:")
        self.input_label.grid(row=0, column=1)
        self.text_input = tk.Text(self.window, height=10, width=30)
        self.text_input.grid(row=1, column=1)
        self.answer_message = tk.Message(self.window, text='The answer will be here', width=300)
        self.answer_message.grid(row=2, column=1)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   width=15, command=self.execdet)
        self.execute_b.grid(row=1, column=2)
    
    def deinit_det(self):
        if self.det_is_init:
            self.input_label.destroy()
            self.text_input.destroy()
            self.answer_message.destroy()
            self.execute_b.destroy()
            self.det_is_init = False

    def execari(self):
        matrix2d1 = Matrix.read(self.text_input1.get("1.0", "end-1c"))
        matrix2d2 = Matrix.read(self.text_input2.get("1.0", "end-1c"))
        operation_str = self.ari_input.get()
        if not (operation_str in ['+', '-', '*', '/']):
            Window.write(self.output_text, "Invalid input")
            return
        try:
            self.solver.change_matrixa(Matrix(matrix2d1))
            self.solver.change_matrixb(Matrix(matrix2d2))
            if operation_str == '+':
                matrix_result = self.solver.getsum()
            elif operation_str == '-':
                matrix_result = self.solver.getsub()
            elif operation_str == '*':
                matrix_result = self.solver.getmult()
            else:
                matrix_result = self.solver.getdiv()
            result = matrix_result.print()
            self.output_text.delete("1.0", "end-1c")
            self.output_text.insert("1.0", result)
        except Exception:
            Window.write(self.output_text, "Invalid input")

    def init_ari(self):
        self.kys()
        self.ari_is_init = True
        self.ari_label = tk.Label(self.window, text="Enter +, - or * below (or even /)")
        self.ari_label.grid(row=0, column=2)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=1)
        self.ari_input = tk.Entry(self.window)
        self.ari_input.grid(row=1, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=3)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   width=15, command=self.execari)
        self.execute_b.grid(row=1, column=4)
        self.output_label = tk.Label(self.window, text="Result:")
        self.output_label.grid(row=2, column=1)
        self.output_text = tk.Text(self.window, height=10, width=30)
        self.output_text.grid(row=2, column=2)

    def deinit_ari(self):
        if self.ari_is_init:
            self.ari_label.destroy()
            self.text_input1.destroy()
            self.ari_input.destroy()
            self.text_input2.destroy()
            self.execute_b.destroy()
            self.output_label.destroy()
            self.output_text.destroy()
            self.ari_is_init = False
    
    def init_linsolve(self):
        self.kys()
        self.linsolve_is_init = True
        self.combo_label = tk.Label(self.window, text="Input Multiplicators")
        self.combo_label.grid(row=0, column=1)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=1)
        self.var_label = tk.Label(self.window, text="Variable Names, Vertically")
        self.var_label.grid(row=0, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=2)
        self.const_label = tk.Label(self.window, text="Input Constants")
        self.const_label.grid(row=0, column=3)
        self.text_input3 = tk.Text(self.window, height=10, width=30)
        self.text_input3.grid(row=1, column=3)
        self.output_label = tk.Label(self.window, text="Output")
        self.output_label.grid(row=2, column=1)
        self.text_output = tk.Text(self.window, height=10, width=30)
        self.text_output.grid(row=2, column=2)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   command=self.execlinsolve)
        self.execute_b.grid(row=2, column=3)
    
    def deinit_linsolve(self):
        if self.linsolve_is_init:
            self.combo_label.destroy()
            self.text_input1.destroy()
            self.var_label.destroy()
            self.text_input2.destroy()
            self.const_label.destroy()
            self.text_input3.destroy()
            self.output_label.destroy()
            self.text_output.destroy()
            self.execute_b.destroy()
            self.linsolve_is_init = False
    
    def execlinsolve(self):
        combo2d = Matrix.read(self.text_input1.get("1.0", "end-1c"))
        varnames = Matrix.read(self.text_input2.get("1.0", "end-1c"), False)
        consts = Matrix.read(self.text_input3.get("1.0", "end-1c"))
        try:
            self.solver.change_matrixa(Matrix(combo2d))
            self.solver.change_matrixb(Matrix(consts))
            solution = Matrix.read(self.solver.linsolve().print(), False)
            result = '\n'.join([' '.join([f"{varnames[i][j]} = {solution[i][j]}"
                                          for j in range(len(solution[0]))])
                                          for i in range(len(solution))])
            Window.write(self.text_output, result)
        except:
            Window.write(self.text_output, "Invalid input")