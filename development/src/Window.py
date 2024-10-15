__name__ = "src.Window"
__package__ = "src"

import tkinter as tk
from Solver import Solver
from Classes.Matrix import Matrix

class Window:
    def getinput(self) -> str:
        return self.text_input.get("1.0", "end-1c")
    
    def writemessage(self, text: str) -> None:
        self.answer_message.config(text=text)
    
    
    def getexec(self, solver: Solver):
        def exec():
            n = int(self.getsize())
            lst = list(map(int, self.getinput().split()))
            matrix_2d = [lst[i*n:(i+1)*n] for i in range(n)]
            solver.matrix1 = Matrix(matrix_2d)
            det = solver.getdet()
            self.writemessage(f"det = {det}")
        return exec

    def __init__(self, solver: Solver):
        self.window = tk.Tk(screenName="LinearSolver",
                                 baseName="LinSol",
                                 className="LinearSolverV01")
        tk.Label(self.window, text="Input size:").grid(row=0, column=0)
        self.size_input = tk.Entry(self.window)
        self.size_input.grid(row=0, column=1)
        self.text_input = tk.Text(self.window, height=10, width=30)
        self.text_input.grid(row=1, column=0)
        self.answer_message = tk.Message(self.window, text='The answer will be here')
        self.answer_message.grid(row=2, column=0)
        self.execute_b = tk.Button(self.window, text="Execute",
                                   width=15, command=self.getexec(solver))
        self.execute_b.grid(row=1, column=1)
        self.window.mainloop()
    
    def getsize(self) -> int:
        return int(self.size_input.get())

    def writemessage(self, text: str) -> None:
        self.answer_message.config(text=text)
    
    def changeexec(self, exec_func) -> None:
        self.execute_b.config(command=exec_func)

