import tkinter as tk

class SubGUI:
    def __init__(self, master: tk.Tk, button: tk.Button):
        self._master = master
        self._button = button
        self._is_init = False
    
    def activate(self):
        self._is_init = True
        self._button.configure(fg="green")

    def collapse(self) -> bool:
        if self._is_init:
            self._button.configure(fg="black")
            return True
        return False

    def calculate(self):
        pass

