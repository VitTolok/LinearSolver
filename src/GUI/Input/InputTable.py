import tkinter as tk
from Classes.Matrix import Matrix


class InputTable:
    """A class that creates and handles an N*M table of entries"""

    def __init__(self, master, rows: int, columns: int, buffer: str | None = None):
        """basic Table setup
        Args:
            master (Any): the window/frame that this table is located inside of
            rows (int): the number of rows
            columns (int): the number of columns
            buffer (str | None, optional): a buffer to fill the table from. Defaults to None.
        """
        self.__master = master
        self.__rows = rows
        self.__columns = columns
        self.__is_init = False
        self.__paste = Matrix.read(buffer, False) if not buffer is None else None

    def activate(self, row: int, column: int):
        """places and builds the table"""
        self.__is_init = True
        self.__submaster = tk.Frame(self.__master, borderwidth=1)
        self.__submaster.grid(row=row, column=column)
        self.__inputs = []
        for i in range(self.__rows):
            tk.Label(self.__submaster, text=str(i + 1)).grid(row=i + 1, column=0)
        for j in range(self.__columns):
            tk.Label(self.__submaster, text=str(j + 1)).grid(row=0, column=j + 1)
        good_width = max(3, round(30 / self.__columns))
        if not self.__paste is None:
            for i in range(self.__rows):
                self.__inputs.append(list())
                for j in range(self.__columns):
                    textvar = tk.StringVar(
                        self.__submaster,
                        value=(
                            self.__paste[i][j]
                            if i < len(self.__paste) and j < len(self.__paste[i])
                            else ""
                        ),
                    )
                    self.__inputs[i].append(
                        tk.Entry(
                            self.__submaster, width=good_width, textvariable=textvar
                        )
                    )
                    self.__inputs[i][j].grid(row=i + 1, column=j + 1)
        else:
            for i in range(self.__rows):
                self.__inputs.append([])
                for j in range(self.__columns):
                    self.__inputs[i].append(
                        tk.Entry(self.__submaster, width=good_width)
                    )
                    self.__inputs[i][j].grid(row=i + 1, column=j + 1)

    def read(self):
        """returns the contents as text"""
        if self.__is_init:
            lst = [
                [self.__inputs[i][j].get() for j in range(self.__columns)]
                for i in range(self.__rows)
            ]
            return "\n".join(
                [
                    " ".join(
                        [lst[i][j].replace(" ", "") for j in range(self.__columns)]
                    ).strip()
                    for i in range(self.__rows)
                ]
            ).strip()
        return ""

    def collapse(self):
        """collapses the table"""
        if self.__is_init:
            self.__submaster.destroy()
