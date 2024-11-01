import tkinter as tk
from GUI.Input.InputField import InputField
from GUI.Input.InputTable import InputTable
from Classes.Matrix import Matrix

class VectorArithmeticsInput(InputField):
    def __init__(self, master, switch_button):
        super().__init__(master, switch_button)
        self._fields = 4
    
    def activate(self, buffers):
        super().activate(buffers)
        self.__basis_1_text = tk.Text(self._master, height=10, width=30)
        self.__batch_1_text = tk.Text(self._master, height=10, width=30)
        self.__basis_2_text = tk.Text(self._master, height=10, width=30)
        self.__batch_2_text = tk.Text(self._master, height=10, width=30)
        self.__basis_1_text.insert("1.0", buffers[0])
        self.__batch_1_text.insert("1.0", buffers[1])
        self.__basis_2_text.insert("1.0", buffers[2])
        self.__batch_2_text.insert("1.0", buffers[3])
        self.__basis_1_text.grid(row=2, column=2)
        self.__batch_1_text.grid(row=2, column=3)
        self.__basis_2_text.grid(row=2, column=5)
        self.__batch_2_text.grid(row=2, column=6)
    
    def _activate_alt(self, buffers):
        super()._activate_alt(buffers)
        dims = max(2, len(Matrix.read(buffers[0])),
                   len(Matrix.read(buffers[1])),
                   len(Matrix.read(buffers[2])),
                   len(Matrix.read(buffers[3])))
        vecs1 = max(1, len(Matrix.read(buffers[1])[0]))
        vecs2 = max(1, len(Matrix.read(buffers[3])[0]))
        self.__dims = tk.IntVar(self._master, value=dims)
        self.__vecs1 = tk.IntVar(self._master, value=vecs1)
        self.__vecs2 = tk.IntVar(self._master, value=vecs2)
        self.__dims_scale = tk.Scale(self._master, variable=self.__dims,
                                     orient='vertical', from_=1, to=10)
        self.__vecs1_scale = tk.Scale(self._master, variable=self.__vecs1,
                                      orient='horizontal', from_=1, to=10)
        self.__vecs2_scale = tk.Scale(self._master, variable=self.__vecs2,
                                      orient='horizontal', from_=1, to=10)
        self.__basis_1_input = InputTable(self._master, dims, dims, buffers[0])
        self.__batch_1_input = InputTable(self._master, dims, vecs1, buffers[1])
        self.__basis_2_input = InputTable(self._master, dims, dims, buffers[2])
        self.__batch_2_input = InputTable(self._master, dims, vecs2, buffers[3])
        self.__resize_button = tk.Button(self._master, text="Resize",
                                         activebackground="green",
                                         command=self.__resize)
        self.__dims_scale.grid(row=2, column=1)
        self.__vecs1_scale.grid(row=1, column=3)
        self.__vecs2_scale.grid(row=1, column=6)
        self.__resize_button.grid(row=1, column=1)
        self.__basis_1_input.activate(2, 2)
        self.__batch_1_input.activate(2, 3)
        self.__basis_2_input.activate(2, 5)
        self.__batch_2_input.activate(2, 6)
    
    def _read_text(self, field = 0):
        if field == 0:
            return self.__basis_1_text.get("1.0", "end-1c")
        if field == 1:
            return self.__batch_1_text.get("1.0", "end-1c")
        if field == 2:
            return self.__basis_2_text.get("1.0", "end-1c")
        return self.__batch_2_text.get("1.0", "end-1c")
    
    def _read_alt(self, field = 0):
        if field == 0:
            return self.__basis_1_input.read()
        if field == 1:
            return self.__batch_1_input.read()
        if field == 2:
            return self.__basis_2_input.read()
        return self.__batch_2_input.read()
    
    def __resize(self):
        dims = self.__dims.get()
        vecs1 = self.__vecs1.get()
        vecs2 = self.__vecs2.get()
        basis_1_buffer = self.__basis_1_input.read()
        batch_1_buffer = self.__batch_1_input.read()
        basis_2_buffer = self.__basis_2_input.read()
        batch_2_buffer = self.__batch_2_input.read()
        self.__basis_1_input.collapse()
        self.__batch_1_input.collapse()
        self.__basis_2_input.collapse()
        self.__batch_2_input.collapse()
        self.__basis_1_input = InputTable(self._master, dims, dims, basis_1_buffer)
        self.__batch_1_input = InputTable(self._master, dims, vecs1, batch_1_buffer)
        self.__basis_2_input = InputTable(self._master, dims, dims, basis_2_buffer)
        self.__batch_2_input = InputTable(self._master, dims, vecs2, batch_2_buffer)
        self.__basis_1_input.activate(2, 2)
        self.__batch_1_input.activate(2, 3)
        self.__basis_2_input.activate(2, 5)
        self.__batch_2_input.activate(2, 6)
    
    def _collapse_text(self):
        if super()._collapse_text():
            self.__basis_1_text.destroy()
            self.__batch_1_text.destroy()
            self.__basis_2_text.destroy()
            self.__batch_2_text.destroy()
    
    def _collapse_alt(self):
        if super()._collapse_alt():
            self.__dims_scale.destroy()
            self.__vecs1_scale.destroy()
            self.__vecs2_scale.destroy()
            self.__resize_button.destroy()
            self.__basis_1_input.collapse()
            self.__batch_1_input.collapse()
            self.__basis_2_input.collapse()
            self.__batch_2_input.collapse()



    
