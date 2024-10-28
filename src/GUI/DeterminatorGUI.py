import tkinter as tk
from GUI.SubGUI import SubGUI
from Classes.Matrix import Matrix

class DeterminatorGUI(SubGUI):
    def __init__(self, master: tk.Tk, button: tk.Button):
        super().__init__(master, button)
        self.__input_buffer = ""
        self.__answer_buffer = "The answer will be here"
        
    def activate(self):
        super().activate()
        self.__input_label = tk.Label(self._master, text="Input square matrix:")
        self.__text_input = tk.Text(self._master, height=10, width=30)
        self.__answer_message = tk.Message(self._master, width=300)
        self.__execute_b = tk.Button(self._master, text="Execute",
                                   activebackground="green",
                                   width=15, command=self.calculate)
        self.__input_label.grid(row=0, column=1)
        self.__text_input.grid(row=1, column=1)
        self.__text_input.insert("1.0", self.__input_buffer)
        self.__answer_message.grid(row=2, column=1)
        self.__answer_message.configure(text=self.__answer_buffer)
        self.__execute_b.grid(row=1, column=2)
    
    def collapse(self):
        if super().collapse():
            self.__input_buffer = self.__text_input.get("1.0", "end-1c")
            self.__answer_buffer = self.__answer_message.cget("text")
            self.__input_label.destroy()
            self.__text_input.destroy()
            self.__answer_message.destroy()
            self.__execute_b.destroy()
    
    def calculate(self):
        try:
            matrix2d = Matrix.read(self.__text_input.get("1.0", "end-1c"))
            matrix = Matrix(matrix2d)
            detmatrix = Matrix([[matrix.det()]])
            self.__answer_message.configure(text=f"det={detmatrix.print()}")
        except Exception:
            self.__answer_message.configure(text="Invalid Input")

    

