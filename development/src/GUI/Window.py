__name__ = "src.GUI.Window"

import tkinter as tk

class Window:
    def __init__(self, execute_command = None):
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
                                   width=15, command=execute_command)
        self.execute_b.grid(row=1, column=1)
        self.window.mainloop()
    
    def getsize(self) -> int:
        return int(self.size_input.get())
    
    def getinput(self) -> str:
        return self.text_input.get(0)

    def writemessage(self, text: str) -> None:
        self.answer_message.setvar("text", text)
    
    def changeexec(self, exec_func) -> None:
        self.execute_b.setvar("command", exec_func)

