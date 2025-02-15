import tkinter as tk
from GUI.SubGUI.DeterminatorGUI import DeterminatorGUI
from GUI.SubGUI.MatrixArithmeticsGUI import MatrixArithmeticsGUI
from GUI.SubGUI.LinearSolverGUI import LinearSolverGUI
from GUI.SubGUI.TransitionSolverGUI.TransitionSolverGUI import TransitionSolverGUI
from GUI.SubGUI.VectorArithmeticsGUI import VectorArithmeticsGUI
from GUI.SubGUI.MatrixGeneratorGUI import MatrixGeneratorGUI

class Window:
    """a class that defines the main window object and allows the user
    to activate parts of the gui"""
    def __init__(self):
        """creates all the main buttons and SubGUI objects"""
        self.__master = tk.Tk(screenName=":0",
                              baseName="LinSol", 
                              className="LinearSolverV0_2")
        self.__det_gui_b = tk.Button(self.__master, text="Determinator",
                                     width=20, activebackground="green")
        self.__matari_gui_b = tk.Button(self.__master, text="Matrix Arithmetics",
                                        width=20, activebackground="green")
        self.__linsol_gui_b = tk.Button(self.__master, text="Linear Equations",
                                        width=20, activebackground="green")
        self.__trans_gui_b = tk.Button(self.__master, text="System Transitions",
                                       width=20, activebackground="green")
        self.__vecari_gui_b = tk.Button(self.__master, text="Vector Arithmetics",
                                        width=20, activebackground="green")
        self.__matgen_gui_b = tk.Button(self.__master, text="Matrix Generator",
                                        width=20, activebackground="green")
        self.__master.grid_columnconfigure(0, minsize=150)
        self.__master.grid_rowconfigure([0, 1, 2, 3, 4, 5], minsize=25)
        self.__det_gui = DeterminatorGUI(self.__master, self.__det_gui_b)
        self.__matari_gui = MatrixArithmeticsGUI(self.__master, self.__matari_gui_b)
        self.__linsol_gui = LinearSolverGUI(self.__master, self.__linsol_gui_b)
        self.__trans_gui = TransitionSolverGUI(self.__master, self.__trans_gui_b)
        self.__vecari_gui = VectorArithmeticsGUI(self.__master, self.__vecari_gui_b)
        self.__matgen_gui = MatrixGeneratorGUI(self.__master, self.__matgen_gui_b)
        self.__det_gui_b.configure(command=self.__activate_det)
        self.__matari_gui_b.configure(command=self.__activate_matari)
        self.__linsol_gui_b.configure(command=self.__activate_linsol)
        self.__trans_gui_b.configure(command=self.__activate_trans)
        self.__vecari_gui_b.configure(command=self.__activate_vecari)
        self.__matgen_gui_b.configure(command=self.__activate_matgen)
        self.__det_gui_b.grid(row=0, column=0)
        self.__matari_gui_b.place_configure(x=0, y=25)
        self.__linsol_gui_b.place_configure(x=0, y=50)
        self.__trans_gui_b.place_configure(x=0, y=75)
        self.__vecari_gui_b.place_configure(x=0, y=100)
        self.__matgen_gui_b.place_configure(x=0, y=125)
        self.__master.mainloop()
    
    def __kys(self):
        """collapses all SubGUI parts, resetting the window"""
        self.__det_gui_b.place_configure(x=0, y=0)
        self.__master.grid_rowconfigure([0, 1, 2, 3, 4, 5], minsize=0)
        self.__det_gui.collapse()
        self.__matari_gui.collapse()
        self.__linsol_gui.collapse()
        self.__trans_gui.collapse()
        self.__vecari_gui.collapse()
        self.__matgen_gui.collapse()
    
    def __activate_det(self):
        """activates the determinator GUI"""
        self.__kys()
        self.__det_gui.activate()
    
    def __activate_matari(self):
        """activates the matrix arithmetics GUI"""
        self.__kys()
        self.__matari_gui.activate()
    
    def __activate_linsol(self):
        """activates the linear equations GUI"""
        self.__kys()
        self.__linsol_gui.activate()
    
    def __activate_trans(self):
        """activates the system transition GUI"""
        self.__kys()
        self.__trans_gui.activate()
    
    def __activate_vecari(self):
        """activates the vector arithmetics GUI"""
        self.__kys()
        self.__vecari_gui.activate()
    
    def __activate_matgen(self):
        """activates the Matrix Generator GUI"""
        self.__kys()
        self.__matgen_gui.activate()
