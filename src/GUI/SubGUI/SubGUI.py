import tkinter as tk


class SubGUI:
    """abstract class that handles basic logic for a part of the GUI"""

    def __init__(self, master: tk.Tk, button: tk.Button):
        """basic setup for a part of the GUI"""
        self._master = master
        self._button = button
        self._is_init = False

    def activate(self):
        """basic logic for the activation of a part of the GUI"""
        self._is_init = True
        self._button.configure(fg="green")

    def collapse(self) -> bool:
        """basic logic for the collapse of a part of the GUI"""
        if self._is_init:
            self._is_init = False
            self._button.configure(fg="black")
            return True
        return False

    def _calculate(self):
        """the method that is supposed to calculate and present the desired answer"""
        pass

    def _write(output: tk.Text, text: str) -> None:
        """a function for overwriting text widget's text"""
        output.delete("1.0", "end-1c")
        output.insert("1.0", text)
