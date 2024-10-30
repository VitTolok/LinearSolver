import tkinter as tk
from Classes.Matrix import Matrix

class InputTable:
    def __init__(self, master, rows: int, columns: int,
                 buffer: str | None = None):
        self.__master = master
        self.__rows = rows
        self.__columns = columns
        self.__is_init = False
        self.__paste = Matrix.read(buffer, False) if not buffer is None else None
    
    def activate(self, row: int, column: int):
        self.__is_init = True
        self.__submaster = tk.Frame(self.__master, borderwidth=10)
        self.__submaster.grid(row=row, column=column)
        self.__inputs = []
        if not self.__paste is None:
            for i in range(self.__rows):
                self.__inputs.append(list())
                for j in range(self.__columns):
                    textvar = tk.StringVar(self.__submaster, value=self.__paste[i][j] 
                               if i < len(self.__paste) and j < len(self.__paste[0])
                               else "")
                    self.__inputs[i].append(tk.Entry(self.__submaster, width=5,
                                                     textvariable=textvar))     
                    self.__inputs[i][j].grid(row=i, column=j)
        else:
            for i in range(self.__rows):
                self.__inputs.append([])
                for j in range(self.__columns):
                    self.__inputs[i].append(tk.Entry(self.__submaster, width=5))
                    self.__inputs[i][j].grid(row=i, column=j)
    
    def read(self):
        if self.__is_init:
            lst = [[self.__inputs[i][j].get() for j in range(self.__columns)]
                for i in range(self.__rows)]
            return '\n'.join([' '.join([lst[i][j].replace(" ", "")
                                        for j in range(self.__columns)]).strip()
                                        for i in range(self.__rows)]).strip()
        return ""
    
    def collapse(self):
        if self.__is_init:
            self.__submaster.destroy()