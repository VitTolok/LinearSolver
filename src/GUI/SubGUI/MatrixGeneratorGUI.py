import tkinter as tk
from GUI.SubGUI.SubGUI import SubGUI
from Classes.Matrix import Matrix

class MatrixGeneratorGUI(SubGUI):
    """a class handling the Matrix Generator part of the GUI"""
    __guide_text = """First line must specify the type of matrix to generate:
    '5E4' means a 4*4 E matrix multplied  by 5'
    '5A4*4' means a 4*4 matrix of all 5's
    You can write any valid python expression before 'E' or 'A',
    standard "math" library included
    'a' and 'b' can be used to refer to the row and column
    iteration of a and b starts with 1"""
    def __init__(self, master, button):
        super().__init__(master, button)
        self.__input_buffer = ""
        self.__output_buffer = ""
    
    def activate(self):
        super().activate()
        self.__input_text = tk.Text(self._master, height=10, width=30)
        self.__output_text = tk.Text(self._master, height=10, width=30)
        self.__input_guide_label = tk.Label(self._master,
                                             text=MatrixGeneratorGUI.__guide_text)
        self.__evaluate = tk.BooleanVar(self._master, value=False)
        self.__evaluate_b = tk.Checkbutton(self._master, variable=self.__evaluate,
                                           text="Evaluate expressions\n(Not recommended)")
        self.__execute_b = tk.Button(self._master, text="Execute",
                                     activebackground="green",
                                     command=self._calculate)
        self.__input_text.insert("1.0", self.__input_buffer)
        self.__output_text.insert("1.0", self.__output_buffer)
        self.__evaluate_b.grid(row=0, column=1)
        self.__input_text.grid(row=1, column=1)
        self.__output_text.grid(row=2, column=1)
        self.__input_guide_label.grid(row=1, column=2)
        self.__execute_b.grid(row=2, column=2)

    def collapse(self):
        if super().collapse():
            self.__input_buffer = self.__input_text.get("1.0", "end-1c")
            self.__output_buffer = self.__output_text.get("1.0", "end-1c")
            self.__input_text.destroy()
            self.__output_text.destroy()
            self.__input_guide_label.destroy()
            self.__evaluate_b.destroy()
            self.__execute_b.destroy()
    
    def _calculate(self):
        try:
            input_lines = self.__input_text.get("1.0", "end-1c").split('\n')
            command = input_lines[0]
            if 'E' in command:
                lst = command.split('E')
                matrix_2d = [[lst[0] if i == j else '0'
                              for j in range(int(lst[1].strip()))]
                              for i in range(int(lst[1].strip()))]
            elif 'A' in command:
                lst = command.split('A')
                mult = lst[0].strip()
                sizes = list(map(int, lst[1].strip().split('*')))
                matrix_2d = [[mult for j in range(sizes[1])] for i in range(sizes[0])]
            else:
                sizes = list(map(int, command[4:].strip().split('*')))
                expr = ''.join(input_lines[1:]).replace(" ", '')
                matrix_2d = [[expr for j in range(sizes[1])]
                              for i in range(sizes[0])]
            result_str = '\n'.join([' '.join(line) for line in matrix_2d])
            if self.__evaluate.get():
                result_str = Matrix(Matrix.read(result_str), True).print()
            SubGUI._write(self.__output_text, result_str)
        except:
            SubGUI._write(self.__output_text, "Invalid Input")
