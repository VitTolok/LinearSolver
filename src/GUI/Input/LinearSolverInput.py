import tkinter as tk
from GUI.Input.InputField import InputField
from GUI.Input.InputTable import InputTable
from Classes.Matrix import Matrix


class LinearSolverInput(InputField):
    """Handles inputs for linear equation part of the GUI"""

    def __init__(self, master, switch_button):
        super().__init__(master, switch_button)
        self._fields = 3

    def activate(self, buffers):
        super().activate(buffers)
        self.__matrix_a_text = tk.Text(self._master, height=10, width=30)
        self.__var_names_text = tk.Text(self._master, height=10, width=30)
        self.__matrix_b_text = tk.Text(self._master, height=10, width=30)
        self.__matrix_a_text.grid(row=1, column=1)
        self.__var_names_text.grid(row=1, column=2)
        self.__matrix_b_text.grid(row=1, column=3)
        self.__matrix_a_text.insert("1.0", buffers[0])
        self.__var_names_text.insert("1.0", buffers[1])
        self.__matrix_b_text.insert("1.0", buffers[2])

    def _activate_alt(self, buffers):
        super()._activate_alt(buffers)
        rows = max(2, len(Matrix.read(buffers[0], False)))
        cols = max(1, len(Matrix.read(buffers[2], False)[0]))
        self.__rows = tk.IntVar(self._master, value=rows)
        self.__cols = tk.IntVar(self._master, value=cols)
        self.__rows_scale = tk.Scale(self._master, variable=self.__rows, from_=1, to=10)
        self.__cols_scale = tk.Scale(
            self._master, variable=self.__cols, from_=1, to=10, orient="horizontal"
        )
        self.__matrix_a_input = InputTable(self._master, rows, rows, buffers[0])
        self.__var_names_input = InputTable(self._master, rows, cols, buffers[1])
        self.__matrix_b_input = InputTable(self._master, rows, cols, buffers[2])
        self.__resize_b = tk.Button(
            self._master, text="Resize", activebackground="green", command=self.__resize
        )
        self.__matrix_a_input.activate(1, 1)
        self.__var_names_input.activate(1, 2)
        self.__matrix_b_input.activate(1, 3)
        self.__rows_scale.grid(row=1, column=4)
        self.__cols_scale.grid(row=0, column=3)
        self.__resize_b.grid(row=1, column=5)

    def _read_text(self, field=0):
        if field == 0:
            return self.__matrix_a_text.get("1.0", "end-1c")
        if field == 1:
            return self.__var_names_text.get("1.0", "end-1c")
        return self.__matrix_b_text.get("1.0", "end-1c")

    def _read_alt(self, field=0):
        if field == 0:
            return self.__matrix_a_input.read()
        if field == 1:
            return self.__var_names_input.read()
        return self.__matrix_b_input.read()

    def __resize(self):
        """triggers size change of the table"""
        rows = self.__rows.get()
        cols = self.__cols.get()
        matrix_a_buffer = self.__matrix_a_input.read()
        var_names_buffer = self.__var_names_input.read()
        matrix_b_buffer = self.__matrix_b_input.read()
        self.__matrix_a_input.collapse()
        self.__var_names_input.collapse()
        self.__matrix_b_input.collapse()
        self.__matrix_a_input = InputTable(self._master, rows, rows, matrix_a_buffer)
        self.__var_names_input = InputTable(self._master, rows, cols, var_names_buffer)
        self.__matrix_b_input = InputTable(self._master, rows, cols, matrix_b_buffer)
        self.__matrix_a_input.activate(1, 1)
        self.__var_names_input.activate(1, 2)
        self.__matrix_b_input.activate(1, 3)

    def _collapse_text(self):
        """collapses text input"""
        if super()._collapse_text():
            self.__matrix_a_text.destroy()
            self.__var_names_text.destroy()
            self.__matrix_b_text.destroy()

    def _collapse_alt(self):
        """collapses table input"""
        if super()._collapse_alt():
            self.__rows_scale.destroy()
            self.__cols_scale.destroy()
            self.__matrix_a_input.collapse()
            self.__var_names_input.collapse()
            self.__matrix_b_input.collapse()
            self.__resize_b.destroy()
