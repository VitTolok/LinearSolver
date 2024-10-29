import tkinter as tk
from GUI.DeterminatorGUI import DeterminatorGUI
from GUI.MatrixArithmeticsGUI import MatrixArithmeticsGUI
from GUI.LinearSolverGUI import LinearSolverGUI
from GUI.TransitionSolverGUI.TransitionSolverGUI import TransitionSolverGUI

class Window:
    def __init__(self):
        self.__master = tk.Tk(screenName="LinearSolver",
                              baseName="LinSol", 
                              className="LinearSolverV0_2")
        self.__det_gui_b = tk.Button(self.__master, text="determinator",
                                     width=20, activebackground="green")
        self.__matari_gui_b = tk.Button(self.__master, text="matrix arithmetics",
                                        width=20, activebackground="green")
        self.__linsol_gui_b = tk.Button(self.__master, text="linear equations",
                                        width=20, activebackground="green")
        self.__trans_gui_b = tk.Button(self.__master, text="System Transitions",
                                       width=20, activebackground="green")
        self.__master.grid_columnconfigure(0, minsize=150)
        self.__master.grid_rowconfigure([0, 1, 2, 3], minsize=25)
        self.__det_gui = DeterminatorGUI(self.__master, self.__det_gui_b)
        self.__matari_gui = MatrixArithmeticsGUI(self.__master, self.__matari_gui_b)
        self.__linsol_gui = LinearSolverGUI(self.__master, self.__linsol_gui_b)
        self.__trans_gui = TransitionSolverGUI(self.__master, self.__trans_gui_b)
        self.__det_gui_b.configure(command=self.__activate_det)
        self.__matari_gui_b.configure(command=self.__activate_matari)
        self.__linsol_gui_b.configure(command=self.__activate_linsol)
        self.__trans_gui_b.configure(command=self.__activate_trans)
        self.__det_gui_b.grid(row=0, column=0)
        self.__matari_gui_b.place_configure(x=0, y=25)
        self.__linsol_gui_b.place_configure(x=0, y=50)
        self.__trans_gui_b.place_configure(x=0, y=75)
        self.__master.mainloop()
    
    def __kys(self):
        self.__det_gui_b.place_configure(x=0, y=0)
        self.__det_gui.collapse()
        self.__matari_gui.collapse()
        self.__linsol_gui.collapse()
        self.__trans_gui.collapse()
    
    def __activate_det(self):
        self.__kys()
        self.__det_gui.activate()
    
    def __activate_matari(self):
        self.__kys()
        self.__matari_gui.activate()
    
    def __activate_linsol(self):
        self.__kys()
        self.__linsol_gui.activate()
    
    def __activate_trans(self):
        self.__kys()
        self.__trans_gui.activate()
