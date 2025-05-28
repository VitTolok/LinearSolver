import tkinter as tk
from GUI.Input.InputField import InputField
from GUI.Input.InputTable import InputTable
from Classes.Matrix import Matrix


class DeterminatorInput(InputField):
    """handles input for Determinator part of the GUI"""

    def activate(self, buffers: list):
        super().activate(buffers)
        self.__text_input = tk.Text(self._master, height=10, width=30)
        self.__text_input.grid(row=1, column=1)
        self.__text_input.insert("1.0", buffers[0])

    def _activate_alt(self, buffers: list):
        super()._activate_alt(buffers)
        size = max(3, len(Matrix.read(buffers[0], False)))
        self.__size = tk.IntVar(self._master, value=size)
        self.__size_scale = tk.Scale(
            self._master, variable=self.__size, from_=1, to=10, orient="horizontal"
        )
        self.__input_table = InputTable(self._master, size, size, buffers[0])
        self.__select_button = tk.Button(
            self._master,
            text="Select",
            activebackground="green",
            width=15,
            command=self.__resize,
        )
        self.__size_scale.grid(row=1, column=1)
        self.__input_table.activate(2, 1)
        self.__select_button.grid(row=1, column=2)

    def __resize(self):
        """triggers size change of the table"""
        size = self.__size.get()
        buffer = self.__input_table.read()
        self.__input_table.collapse()
        self.__input_table = InputTable(self._master, size, size, buffer)
        self.__input_table.activate(2, 1)

    def _collapse_text(self):
        """collapses text input"""
        if super()._collapse_text():
            self.__text_input.destroy()

    def _collapse_alt(self):
        """collapses table input"""
        if super()._collapse_alt():
            self.__size_scale.destroy()
            self.__input_table.collapse()
            self.__select_button.destroy()

    def _read_text(self, field=0):
        return self.__text_input.get("1.0", "end-1c")

    def _read_alt(self, field=0):
        return self.__input_table.read()
