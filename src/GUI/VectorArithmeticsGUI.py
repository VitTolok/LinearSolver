import tkinter as tk
from GUI.SubGUI import SubGUI
from GUI.Input.VectorArithmeticsInput import VectorArithmeticsInput
from Solver.VectorArithmeticsSolver import VectorArithmeticsSolver
from Classes.Matrix import Matrix

class VectorArithmeticsGUI(SubGUI):
    def __init__(self, master, button):
        super().__init__(master, button)
        self.__basis_1_buffer = ""
        self.__batch_1_buffer = ""
        self.__basis_2_buffer = ""
        self.__batch_2_buffer = ""
        self.__output_buffer = ""
    
    def activate(self):
        super().activate()
        self.__basis_1_label = tk.Label(self._master, text="Basis of the 1st batch:")
        self.__batch_1_label = tk.Label(self._master, text="The first batch:")
        self.__basis_2_label = tk.Label(self._master, text="Basis of the 2nd batch:")
        self.__batch_2_label = tk.Label(self._master, text="The second batch:")
        self.__alt_input_button = tk.Button(self._master, text="Alt Input",
                                            activebackground="green")
        self.__input = VectorArithmeticsInput(self._master,
                                              self.__alt_input_button)
        self.__operator_input = tk.Entry(self._master, width=5)
        self.__output_text = tk.Text(self._master, height=10, width=30)
        self.__execute_button = tk.Button(self._master, text="Execute",
                                          activebackground="green",
                                          command=self._calculate)
        self.__input.activate([self.__basis_1_buffer,
                               self.__batch_1_buffer,
                               self.__basis_2_buffer,
                               self.__batch_2_buffer])
        self.__output_text.insert("1.0", self.__output_buffer)
        self.__basis_1_label.grid(row=0, column=2)
        self.__batch_1_label.grid(row=0, column=3)
        self.__operator_input.grid(row=2, column=4)
        self.__basis_2_label.grid(row=0, column=5)
        self.__batch_2_label.grid(row=0, column=6)
        self.__alt_input_button.grid(row=0, column=7)
        self.__execute_button.grid(row=3, column=5)
        self.__output_text.grid(row=3, column=3)
    
    def collapse(self):
        if super().collapse():
            self.__basis_1_buffer = self.__input.read(0)
            self.__batch_1_buffer = self.__input.read(1)
            self.__basis_2_buffer = self.__input.read(2)
            self.__batch_2_buffer = self.__input.read(3)
            self.__output_buffer = self.__output_text.get("1.0", "end-1c")
            self.__input.collapse()
            self.__basis_1_label.destroy()
            self.__batch_1_label.destroy()
            self.__basis_2_label.destroy()
            self.__batch_2_label.destroy()
            self.__alt_input_button.destroy()
            self.__operator_input.destroy()
            self.__output_text.destroy()
            self.__execute_button.destroy()
    
    def _calculate(self):
        try:
            basis_1_text = self.__input.read(0)
            batch_1_text = self.__input.read(1)
            basis_2_text = self.__input.read(2)
            batch_2_text = self.__input.read(3)
            basis_1 = Matrix(Matrix.read(basis_1_text)) if basis_1_text != "" else None
            batch_1 = Matrix(Matrix.read(batch_1_text)) if batch_1_text != "" else None
            basis_2 = Matrix(Matrix.read(basis_2_text)) if basis_2_text != "" else None
            batch_2 = Matrix(Matrix.read(batch_2_text)) if batch_2_text != "" else None
            solver = VectorArithmeticsSolver([basis_1, batch_1, basis_2, batch_2])
            operator = self.__operator_input.get().strip()
            if operator[0] == "+":
                result = solver.add(int(operator[1]) if len(operator)==2 else 0).print()
            elif operator[0] == "-":
                result = solver.sub(int(operator[1]) if len(operator)==2 else 0).print()
            elif operator == "(*)":
                result = Matrix([[solver.scalmult()]]).print()
            elif operator == "(*]" or operator == "[*)":
                result = Matrix([[solver.mixmult()]]).print()
            elif operator == "[*]":
                result = solver.vectormult().tomatrix().print()
            elif operator == "[/]":
                result == "TBA"
            else:
                result == "Invalid operator"
            SubGUI._write(self.__output_text, result)
        except Exception:
            SubGUI._write(self.__output_text, "Invalid Input")




        

