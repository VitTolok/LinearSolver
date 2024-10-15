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
        self.window.mainloop()
    
    def __noinit(self):
        self.det_is_init = False
        self.ari_is_init = False
    
    def kys(self):
        self.deinit_det()
        self.deinit_ari()

    def execdet(self):
        n = int(self.size_input.get())
        lst = list(map(int, self.text_input.get("1.0", "end-1c").split()))
        matrix_2d = [lst[i*n:(i+1)*n] for i in range(n)]
        self.solver.change_matrix1(Matrix(matrix_2d))
        det = self.solver.getdet1()
        self.answer_message.config(text=f"det = {det}")
    

    def init_det(self):
        self.kys()
        self.det_is_init = True
        self.size_label = tk.Label(self.window, text="Input size:")
        self.size_label.grid(row=0, column=1)
        self.size_input = tk.Entry(self.window)
        self.size_input.grid(row=0, column=2)
        self.text_input = tk.Text(self.window, height=10, width=30)
        self.text_input.grid(row=1, column=1)
        self.answer_message = tk.Message(self.window, text='The answer will be here', width=300)
        self.answer_message.grid(row=2, column=1)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   width=15, command=self.execdet)
        self.execute_b.grid(row=1, column=2)
    
    def deinit_det(self):
        if self.det_is_init:
            self.size_label.destroy()
            self.size_input.destroy()
            self.text_input.destroy()
            self.answer_message.destroy()
            self.execute_b.destroy()

    def execari(self):
        lst1 = self.text_input1.get("1.0", "end-1c").split('\n')
        lst2 = self.text_input2.get("1.0", "end-1c").split('\n')
        if '' in lst1 or '' in lst2:
            self.output_text.delete("1.0", "end-1c")
            self.output_text.insert("1.0", "no newlines at the end")
            return
        operation_str = self.ari_input.get()
        if not (operation_str in ['+', '-', '*']):
            self.output_text.delete("1.0", "end-1c")
            self.output_text.insert("1.0", "invalid operation")
            return
        matrix2d1 = [list(map(int, line.split())) for line in lst1]
        matrix2d2 = [list(map(int, line.split())) for line in lst2]
        self.solver.change_matrix1(Matrix(matrix2d1))
        self.solver.change_matrix2(Matrix(matrix2d2))
        if operation_str == '+':
            matrix_result = self.solver.getsum()
        elif operation_str == '-':
            matrix_result = self.solver.getsub()
        else:
            matrix_result = self.solver.getmult()
        result = '\n'.join([' '.join(list(map(str, line)))
                            for line in matrix_result._tolist()])
        self.output_text.delete("1.0", "end-1c")
        self.output_text.insert("1.0", result)

        
    
    def init_ari(self):
        self.kys()
        self.ari_is_init = True
        self.ari_label = tk.Label(self.window, text="Enter +, - or * below")
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