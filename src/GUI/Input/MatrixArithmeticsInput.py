import tkinter as tk
from GUI.Input.InputField import InputField
from GUI.Input.InputTable import InputTable
from Classes.Matrix import Matrix

class MatrixArithmeticsInput(InputField):
    def __init__(self, master, switch_button):
        super().__init__(master, switch_button)
        self._fields = 2
    
    def activate(self, buffers):
        super().activate(buffers)
        self.__text_input_1 = tk.Text(self._master, height=10, width=30)
        self.__text_input_2 = tk.Text(self._master, height=10, width=30)
        self.__text_input_1.grid(row=1, column=2)
        self.__text_input_2.grid(row=1, column=4)
        self.__text_input_1.insert("1.0", buffers[0])
        self.__text_input_2.insert("1.0", buffers[1])
    
    def _activate_alt(self, buffers):
        super()._activate_alt(buffers)
        rows1 = max(3, len(Matrix.read(buffers[0], False)))
        rows2 = max(3, len(Matrix.read(buffers[1], False)))
        cols1 = max(3, len(Matrix.read(buffers[0], False)[0]))
        cols2 = max(3, len(Matrix.read(buffers[1], False)[0]))
        self.__rows1 = tk.IntVar(self._master, value=rows1)
        self.__rows2 = tk.IntVar(self._master, value=rows2)
        self.__cols1 = tk.IntVar(self._master, value=cols1)
        self.__cols2 = tk.IntVar(self._master, value=cols2)
        self.__rows1_scale = tk.Scale(self._master, variable=self.__rows1,
                                      from_=1, to=10)
        self.__rows2_scale = tk.Scale(self._master, variable=self.__rows2,
                                      from_=1, to=10)
        self.__cols1_scale = tk.Scale(self._master, variable=self.__cols1,
                                      orient='horizontal', from_=1, to=10)
        self.__cols2_scale = tk.Scale(self._master, variable=self.__cols2,
                                      orient='horizontal', from_=1, to=10)
        self.__input_1 = InputTable(self._master, rows1, cols1, buffers[0])
        self.__input_2 = InputTable(self._master, rows2, cols2, buffers[1])
        self.__resize_b = tk.Button(self._master, text="Resize",
                                    activebackground="green",
                                    width=15, command=self.__resize)
        self.__input_1.activate(1, 2)
        self.__input_2.activate(1, 4)
        self.__rows1_scale.grid(row=1, column=1)
        self.__rows2_scale.grid(row=1, column=5)
        self.__cols1_scale.grid(row=0, column=2)
        self.__cols2_scale.grid(row=0, column=4)
        self.__resize_b.grid(row=1, column=6)

    def _read_text(self, field = 0):
        if field == 0:
            return self.__text_input_1.get("1.0", "end-1c")
        return self.__text_input_2.get("1.0", "end-1c")
    
    def _read_alt(self, field = 0):
        if field == 0:
            return self.__input_1.read()
        return self.__input_2.read()
    
    def __resize(self):
        rows1 = self.__rows1.get()
        cols1 = self.__cols1.get()
        rows2 = self.__rows2.get()
        cols2 = self.__cols2.get()
        buffer1 = self.__input_1.read()
        buffer2 = self.__input_2.read()
        self.__input_1.collapse()
        self.__input_2.collapse()
        self.__input_1 = InputTable(self._master, rows1, cols1, buffer1)
        self.__input_2 = InputTable(self._master, rows2, cols2, buffer2)
        self.__input_1.activate(1, 2)
        self.__input_2.activate(1, 4)
    
    def _collapse_text(self):
        if super()._collapse_text():
            self.__text_input_1.destroy()
            self.__text_input_2.destroy()
    
    def _collapse_alt(self):
        if super()._collapse_alt():
            self.__rows1_scale.destroy()
            self.__rows2_scale.destroy()
            self.__cols1_scale.destroy()
            self.__cols2_scale.destroy()
            self.__input_1.collapse()
            self.__input_2.collapse()
            self.__resize_b.destroy()



    
    