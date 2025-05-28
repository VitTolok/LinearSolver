import tkinter as tk
from GUI.SubGUI.SubGUI import SubGUI
from GUI.Input.DeterminatorInput import DeterminatorInput
from Classes.Matrix import Matrix


class DeterminatorGUI(SubGUI):
    """a class handling the Determinator part of the GUI"""

    def __init__(self, master: tk.Tk, button: tk.Button):
        super().__init__(master, button)
        self.__input_buffer = ""
        self.__answer_buffer = "The answer will be here"

    def activate(self):
        super().activate()
        self.__input_label = tk.Label(self._master, text="Input square matrix:")
        self.__execute_b = tk.Button(
            self._master,
            text="Execute",
            activebackground="green",
            width=15,
            command=self._calculate,
        )
        self.__alternate_b = tk.Button(
            self._master, text="Alt Input", activebackground="green", width=15
        )
        self.__input = DeterminatorInput(self._master, self.__alternate_b)
        self.__answer_message = tk.Message(self._master, width=300)
        self.__alternate_b.grid(row=0, column=2)
        self.__input_label.grid(row=0, column=1)
        self.__input.activate([self.__input_buffer])
        self.__answer_message.grid(row=3, column=1)
        self.__answer_message.configure(text=self.__answer_buffer)
        self.__execute_b.grid(row=2, column=2)

    def collapse(self):
        if super().collapse():
            self.__input_label.destroy()
            self.__input_buffer = self.__input.read()
            self.__input.collapse()
            self.__answer_message.destroy()
            self.__execute_b.destroy()
            self.__alternate_b.destroy()

    def _calculate(self):
        try:
            matrix2d = Matrix.read(self.__input.read())
            matrix = Matrix(matrix2d)
            detmatrix = Matrix([[matrix.det()]])
            self.__answer_message.configure(text=f"det = {detmatrix.print()}")
            self.__answer_buffer = f"det = {detmatrix.print()}"
        except Exception:
            self.__answer_message.configure(text="Invalid Input")
        if Matrix.sizeof_detcache() > 1_073_741_824:  # 1GB
            Matrix.clear_detcache()
