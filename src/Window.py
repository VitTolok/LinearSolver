import tkinter as tk
from Solver import Solver
from Classes.Matrix import Matrix
from Classes.Vector import Vector

class Window:
    
    def __init__(self, solver: Solver):
        self.__noinit()
        self.solver = solver
        self.window = tk.Tk(screenName="LinearSolver",
                                 baseName="LinSol",
                                 className="LinearSolverV0_1")
        self.init_det_b = tk.Button(self.window, text="determinator",
                                    command=self.init_det,
                                    activebackground="green")
        self.init_det_b.grid(row=0, column=0)
        self.init_ari_b = tk.Button(self.window, text="matrix arithmetics",
                                    command=self.init_ari,
                                    activebackground="green")
        self.init_ari_b.grid(row=1, column=0)
        self.init_linsolve_b = tk.Button(self.window, text="Linear Equations",
                                        command=self.init_linsolve,
                                        activebackground="green")
        self.init_linsolve_b.grid(row=2, column=0)
        self.init_trans_b = tk.Button(self.window, text="Basis transitions",
                                        command=self.init_trans,
                                        activebackground="green")
        self.init_trans_b.grid(row=3, column=0)
        self.window.mainloop()
    
    def __noinit(self):
        self.det_is_init = False
        self.ari_is_init = False
        self.linsolve_is_init = False
        self.trans_is_init = False
    
    def kys(self):
        self.deinit_det()
        self.deinit_ari()
        self.deinit_linsolve()
        self.deinit_trans()

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
        self.init_det_b.configure(fg="green")
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
            self.init_det_b.configure(fg="black")
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
                matrix_result = self.solver.getsummat()
            elif operation_str == '-':
                matrix_result = self.solver.getsubmat()
            elif operation_str == '*':
                matrix_result = self.solver.getmultmat()
            else:
                matrix_result = self.solver.getdivmat()
            result = matrix_result.print()
            self.output_text.delete("1.0", "end-1c")
            self.output_text.insert("1.0", result)
        except Exception:
            Window.write(self.output_text, "Invalid input")

    def init_ari(self):
        self.kys()
        self.ari_is_init = True
        self.init_ari_b.configure(fg="green")
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
            self.init_ari_b.configure(fg="black")
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
        self.init_linsolve_b.configure(fg="green")
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
            self.init_linsolve_b.configure(fg="black")
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
    
    def init_trans(self):
        self.kys()
        self.trans_is_init = True
        self.init_trans_b.configure(fg="green")
        self.basis_known_b = tk.Button(self.window, text="Basis known",
                                       command=self.init_trans_basis_known,
                                       fg="green")
        self.basis_known_b.grid(row=0, column=1)
        self.basis_unknown_b = tk.Button(self.window, text="Points known",
                                       command=self.init_trans_basis_unknown)
        self.basis_unknown_b.grid(row=1, column=1)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=3)
        self.text_input3 = tk.Text(self.window, height=10, width=30)
        self.text_input3.grid(row=1, column=4)
        self.text_output = tk.Text(self.window, height=10, width=30)
        self.text_output.grid(row=2, column=3)
        self.trans_label1 = tk.Label(self.window, text="First Basis:")
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(self.window,
                                     text="Vector in first basis:\n(Nothing for transition matrix)")
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(self.window, text="Second Basis:")
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   command=self.exectrans)
        self.execute_b.grid(row=2, column=4)

    def init_trans_basis_unknown(self):
        self.trans_label1.destroy()
        self.trans_label2.destroy()
        self.trans_label3.destroy()
        self.execute_b.destroy()
        self.basis_known_b.configure(fg="black")
        self.basis_unknown_b.configure(fg="green")
        self.trans_label1 = tk.Label(self.window, text="Known common points in basis 1:")
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(self.window,
                                     text="Vector in first basis:\n(Nothing for transition matrix)")
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(self.window, text="Known common points in basis 2:")
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   command=self.execuktrans)
        self.execute_b.grid(row=2, column=4)

    def init_trans_basis_known(self):
        self.trans_label1.destroy()
        self.trans_label2.destroy()
        self.trans_label3.destroy()
        self.execute_b.destroy()
        self.basis_known_b.configure(fg="green")
        self.basis_unknown_b.configure(fg="black")
        self.trans_label1 = tk.Label(self.window, text="First Basis:")
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(self.window,
                                     text="Point in first CS:")
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(self.window, text="Second Basis:")
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   command=self.exectrans)
        self.execute_b.grid(row=2, column=4)

    def deinit_trans(self):
        if self.trans_is_init:
            self.trans_is_init = False
            self.init_trans_b.configure(fg="black")
            self.basis_known_b.destroy()
            self.basis_unknown_b.destroy()
            self.text_input1.destroy()
            self.text_input2.destroy()
            self.text_input3.destroy()
            self.text_output.destroy()
            self.trans_label1.destroy()
            self.trans_label2.destroy()
            self.trans_label3.destroy()
            self.execute_b.destroy()

    def exectrans(self):
        try:
            basis1 = Matrix(Matrix.read(self.text_input1.get("1.0", "end-1c")))
            veclst = self.text_input2.get("1.0", "end-1c").split()
            basis2 = Matrix(Matrix.read(self.text_input3.get("1.0", "end-1c")))
            self.solver.change_matrixa(basis1)
            self.solver.change_matrixb(basis2)
            if veclst == [] or veclst == ['']:
                Window.write(self.text_output, self.solver.transmat().print())
            else:
                vector = Vector(veclst, basis1)
                self.solver.change_vectora(vector)
                Window.write(self.text_output, self.solver.transvec().print())
        except Exception:
            Window.write(self.text_output, "Invalid input")

    def execuktrans(self):
        try:
            self.solver.change_matrixa(Matrix(Matrix.read(
                                       self.text_input1.get("1.0", "end-1c"))))
            self.solver.change_vectora(Vector(self.text_input2.get("1.0", "end-1c").split()))
            self.solver.change_matrixb(Matrix(Matrix.read(
                                       self.text_input3.get("1.0", "end-1c"))))
            Window.write(self.text_output, self.solver.transpoints().print())
        except Exception:
            Window.write(self.text_output, "Invalid input")
