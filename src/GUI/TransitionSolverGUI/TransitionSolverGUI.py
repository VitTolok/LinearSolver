import tkinter as tk
from GUI.SubGUI import SubGUI
from GUI.TransitionSolverGUI.BasisTransitionGUI import BasisTransitionGUI
from GUI.TransitionSolverGUI.CoordinateTransitionGUI import CoordinateTransitionGUI

class TransitionSolverGUI(SubGUI):
    def __init__(self, master, button):
        super().__init__(master, button)
        self.__basis_gui = BasisTransitionGUI(self._master, None)
        self.__coord_gui = CoordinateTransitionGUI(self._master, None)
    
    def activate(self):
        super().activate()
        self.__basis_gui_b = tk.Button(self._master, text="Basis Transitions",
                                       command=self.__activate_basis, width=20,
                                       activebackground="green")
        self.__coord_gui_b = tk.Button(self._master, text="Coordinate Transitions",
                                       command=self.__activate_coord, width=20,
                                       activebackground="green")
        self.__basis_gui._button = self.__basis_gui_b
        self.__coord_gui._button = self.__coord_gui_b
        self._master.columnconfigure(1, minsize=150)
        self.__basis_gui_b.grid(row=0, column=1)
        self.__coord_gui_b.place_configure(x=150, y=25)
        self._master.grid_rowconfigure([0, 1, 2, 3, 4, 5], minsize=25)
    
    def collapse(self):
        if super().collapse():
            self._master.columnconfigure(1, minsize=0)
            self.__basis_gui.collapse()
            self.__coord_gui.collapse()
            self.__basis_gui_b.destroy()
            self.__coord_gui_b.destroy()
    
    def __activate_basis(self):
        self.__basis_gui_b.place_configure(x=150, y=0)
        self.__coord_gui.collapse()
        self.__basis_gui.activate()
    
    def __activate_coord(self):
        self.__basis_gui_b.place_configure(x=150, y=0)
        self.__basis_gui.collapse()
        self.__coord_gui.activate()