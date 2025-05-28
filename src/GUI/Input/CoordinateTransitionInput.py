import tkinter as tk
from GUI.Input.InputField import InputField
from GUI.Input.InputTable import InputTable
from Classes.Matrix import Matrix


class CoordinateTransitionInput(InputField):
    """Handles input for Coordinate transition part of the GUI"""

    def __init__(self, master, switch_button):
        super().__init__(master, switch_button)
        self._fields = 3

    def activate(self, buffers):
        super().activate(buffers)
        self.__system_1_text = tk.Text(self._master, height=10, width=30)
        self.__batch_text = tk.Text(self._master, height=10, width=30)
        self.__system_2_text = tk.Text(self._master, height=10, width=30)
        self.__system_1_text.insert("1.0", buffers[0])
        self.__batch_text.insert("1.0", buffers[1])
        self.__system_2_text.insert("1.0", buffers[2])
        self.__system_1_text.grid(row=1, column=2)
        self.__batch_text.grid(row=1, column=3)
        self.__system_2_text.grid(row=1, column=5)

    def _activate_alt(self, buffers):
        super()._activate_alt(buffers)
        rows = max(2, len(Matrix.read(buffers[0], False)))
        cols = max(1, len(Matrix.read(buffers[1], False)[0]))
        self.__rows = tk.IntVar(self._master, value=rows)
        self.__cols = tk.IntVar(self._master, value=cols)
        self.__rows_scale = tk.Scale(self._master, variable=self.__rows, from_=1, to=10)
        self.__cols_scale = tk.Scale(
            self._master, variable=self.__cols, orient="horizontal", from_=1, to=10
        )
        self.__system_1_input = InputTable(self._master, rows, rows + 1, buffers[0])
        self.__batch_input = InputTable(self._master, rows, cols, buffers[1])
        self.__system_2_input = InputTable(self._master, rows, rows + 1, buffers[2])
        self.__resize_button = tk.Button(
            self._master, text="Resize", activebackground="green", command=self.__resize
        )
        self.__system_1_input.activate(2, 2)
        self.__batch_input.activate(2, 3)
        self.__system_2_input.activate(2, 5)
        self.__rows_scale.grid(row=2, column=4)
        self.__cols_scale.grid(row=1, column=3)
        self.__resize_button.grid(row=1, column=4)

    def _read_text(self, field=0):
        if field == 0:
            return self.__system_1_text.get("1.0", "end-1c")
        if field == 1:
            return self.__batch_text.get("1.0", "end-1c")
        return self.__system_2_text.get("1.0", "end-1c")

    def _read_alt(self, field=0):
        if field == 0:
            return self.__system_1_input.read()
        if field == 1:
            return self.__batch_input.read()
        return self.__system_2_input.read()

    def __resize(self):
        """triggers size change of the table"""
        rows = self.__rows.get()
        cols = self.__cols.get()
        basis_1_buffer = self.__system_1_input.read()
        batch_buffer = self.__batch_input.read()
        basis_2_buffer = self.__system_2_input.read()
        self.__system_1_input.collapse()
        self.__batch_input.collapse()
        self.__system_2_input.collapse()
        self.__system_1_input = InputTable(self._master, rows, rows + 1, basis_1_buffer)
        self.__batch_input = InputTable(self._master, rows, cols, batch_buffer)
        self.__system_2_input = InputTable(self._master, rows, rows + 1, basis_2_buffer)
        self.__system_1_input.activate(2, 2)
        self.__batch_input.activate(2, 3)
        self.__system_2_input.activate(2, 5)

    def _collapse_text(self):
        """collapses text input"""
        if super()._collapse_text():
            self.__system_1_text.destroy()
            self.__batch_text.destroy()
            self.__system_2_text.destroy()

    def _collapse_alt(self):
        """collapses table input"""
        if super()._collapse_alt():
            self.__rows_scale.destroy()
            self.__cols_scale.destroy()
            self.__system_1_input.collapse()
            self.__batch_input.collapse()
            self.__system_2_input.collapse()
            self.__resize_button.destroy()
