import tkinter

class Window:
    def __init__(self):
        self.window = tkinter.Tk(screenName="LinearSolver",
                                 baseName="LinSol",
                                 className="LinearSolverV0.1")
        self.window.mainloop()