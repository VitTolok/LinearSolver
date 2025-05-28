import tkinter as tk
from Solver.Solver import oldSolver
from Classes.Matrix import Matrix
from Classes.Vector import Vector


class oldWindow:
    """A deprecated class for operating GUI, including reading, writing,
    conversion of data for further calculation, calling for calculation
    """

    def __init__(self):
        """Creates a new window with base GUI and a Solver entity"""
        self.__noinit()
        self.solver = oldSolver()
        self.window = tk.Tk(
            screenName="LinearSolver", baseName="LinSol", className="LinearSolverV0_1"
        )
        self.window.grid_columnconfigure(0, minsize=150)
        self.window.grid_rowconfigure([0, 1, 2, 3, 4], minsize=25)
        self.init_det_b = tk.Button(
            self.window,
            text="determinator",
            command=self.init_det,
            width=20,
            activebackground="green",
        )
        self.init_det_b.place_configure(x=0, y=0)
        self.init_ari_b = tk.Button(
            self.window,
            text="matrix arithmetics",
            command=self.init_ari,
            width=20,
            activebackground="green",
        )
        self.init_ari_b.place_configure(x=0, y=25)
        self.init_linsolve_b = tk.Button(
            self.window,
            text="Linear Equations",
            command=self.init_linsolve,
            width=20,
            activebackground="green",
        )
        self.init_linsolve_b.place_configure(x=0, y=50)
        self.init_trans_b = tk.Button(
            self.window,
            text="Basis transitions",
            command=self.init_trans,
            width=20,
            activebackground="green",
        )
        self.init_trans_b.place_configure(x=0, y=75)
        self.init_vecari_b = tk.Button(
            self.window,
            text="Vector arithmetics",
            command=self.init_vecari,
            width=20,
            activebackground="green",
        )
        self.init_vecari_b.place_configure(x=0, y=100)
        self.window.mainloop()

    def __noinit(self) -> None:
        """Declares all GUI parts as uninitialised"""
        self.det_is_init = False
        self.ari_is_init = False
        self.linsolve_is_init = False
        self.trans_is_init = False
        self.vecari_is_init = False

    def kys(self) -> None:
        """Deinitialises all gui parts, removing them from the window"""
        self.deinit_det()
        self.deinit_ari()
        self.deinit_linsolve()
        self.deinit_trans()
        self.deinit_vecari()

    def write(output: tk.Text, text: str) -> None:
        """Writes the string of text into a Text widjet,
        removing everything else from it
        Args:
            output (tk.Text): the target Text widjet
            text (str): the string to write
        """
        output.delete("1.0", "end-1c")
        output.insert("1.0", text)

    def execdet(self) -> None:
        """Commences determinant calculation by reading the matrix and calling solver
        The det part of the gui has to be init
        """
        matrix_2d = Matrix.read(self.text_input.get("1.0", "end-1c"))
        try:
            self.solver.change_matrixa(Matrix(matrix_2d))
            det = self.solver.getdeta()
            if isinstance(det, complex):
                det = complex(round(det.real, 4), round(det.imag, 4))
                if det.imag == 0:
                    det = det.real
            if isinstance(det, float):
                if int(det) == det:
                    det = int(det)
            self.answer_message.config(text=f"det = {det}")
        except Exception:
            self.answer_message.config(text="Invalid Input")

    def init_det(self) -> None:
        """Initialises the det calculation part of the GUI"""
        self.kys()
        self.det_is_init = True
        self.init_det_b.configure(fg="green")
        self.input_label = tk.Label(self.window, text="Input square matrix:")
        self.input_label.grid(row=0, column=1)
        self.text_input = tk.Text(self.window, height=10, width=30)
        self.text_input.grid(row=1, column=1)
        self.answer_message = tk.Message(
            self.window, text="The answer will be here", width=300
        )
        self.answer_message.grid(row=2, column=1)
        self.execute_b = tk.Button(
            self.window, text="Execute", width=15, command=self.execdet
        )
        self.execute_b.grid(row=1, column=2)

    def deinit_det(self) -> None:
        """Deinitialises the det calculation part of the GUI"""
        if self.det_is_init:
            self.init_det_b.configure(fg="black")
            self.input_label.destroy()
            self.text_input.destroy()
            self.answer_message.destroy()
            self.execute_b.destroy()
            self.det_is_init = False

    def execari(self) -> None:
        """Commences matrix arithmetics by calling the appropriate solver algo
        ari part of the GUI has to be init
        """
        matrix2d1 = Matrix.read(self.text_input1.get("1.0", "end-1c"))
        matrix2d2 = Matrix.read(self.text_input2.get("1.0", "end-1c"))
        operation_str = self.ari_input.get()
        if not (operation_str in ["+", "-", "*", "/"]):
            oldWindow.write(self.output_text, "Invalid input")
            return
        try:
            self.solver.change_matrixa(Matrix(matrix2d1))
            self.solver.change_matrixb(Matrix(matrix2d2))
            if operation_str == "+":
                matrix_result = self.solver.getsummat()
            elif operation_str == "-":
                matrix_result = self.solver.getsubmat()
            elif operation_str == "*":
                matrix_result = self.solver.getmultmat()
            else:
                matrix_result = self.solver.getdivmat()
            result = matrix_result.print()
            self.output_text.delete("1.0", "end-1c")
            self.output_text.insert("1.0", result)
        except Exception:
            oldWindow.write(self.output_text, "Invalid input")

    def init_ari(self):
        """inits the ari part of the GUI"""
        self.kys()
        self.ari_is_init = True
        self.init_ari_b.configure(fg="green")
        self.ari_label = tk.Label(self.window, text="Enter +, - or * below (or even /)")
        self.ari_label.grid(row=0, column=2)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=1)
        self.ari_input = tk.Entry(self.window)
        self.ari_input.grid(row=1, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=3)
        self.execute_b = tk.Button(
            self.window, text="Execute", width=15, command=self.execari
        )
        self.execute_b.grid(row=1, column=4)
        self.output_label = tk.Label(self.window, text="Result:")
        self.output_label.grid(row=2, column=1)
        self.output_text = tk.Text(self.window, height=10, width=30)
        self.output_text.grid(row=2, column=2)

    def deinit_ari(self):
        """deinits the ari part of the GUI"""
        if self.ari_is_init:
            self.init_ari_b.configure(fg="black")
            self.ari_label.destroy()
            self.text_input1.destroy()
            self.ari_input.destroy()
            self.text_input2.destroy()
            self.execute_b.destroy()
            self.output_label.destroy()
            self.output_text.destroy()
            self.ari_is_init = False

    def init_linsolve(self):
        """inits the linsolve part of the gui"""
        self.kys()
        self.linsolve_is_init = True
        self.init_linsolve_b.configure(fg="green")
        self.combo_label = tk.Label(self.window, text="Input Multiplicators")
        self.combo_label.grid(row=0, column=1)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=1)
        self.var_label = tk.Label(self.window, text="Variable Names, Vertically")
        self.var_label.grid(row=0, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=2)
        self.const_label = tk.Label(self.window, text="Input Constants")
        self.const_label.grid(row=0, column=3)
        self.text_input3 = tk.Text(self.window, height=10, width=30)
        self.text_input3.grid(row=1, column=3)
        self.output_label = tk.Label(self.window, text="Output")
        self.output_label.grid(row=2, column=1)
        self.text_output = tk.Text(self.window, height=10, width=30)
        self.text_output.grid(row=2, column=2)
        self.execute_b = tk.Button(
            self.window, text="Execute", command=self.execlinsolve
        )
        self.execute_b.grid(row=2, column=3)

    def deinit_linsolve(self):
        """deinits the linsolve part of the GUI"""
        if self.linsolve_is_init:
            self.init_linsolve_b.configure(fg="black")
            self.combo_label.destroy()
            self.text_input1.destroy()
            self.var_label.destroy()
            self.text_input2.destroy()
            self.const_label.destroy()
            self.text_input3.destroy()
            self.output_label.destroy()
            self.text_output.destroy()
            self.execute_b.destroy()
            self.linsolve_is_init = False

    def execlinsolve(self):
        """Commences solution of a linear system by calling Solver"""
        combo2d = Matrix.read(self.text_input1.get("1.0", "end-1c"))
        varnames = Matrix.read(self.text_input2.get("1.0", "end-1c"), False)
        consts = Matrix.read(self.text_input3.get("1.0", "end-1c"))
        try:
            self.solver.change_matrixa(Matrix(combo2d))
            self.solver.change_matrixb(Matrix(consts))
            solution = Matrix.read(self.solver.linsolve().print(), False)
            result = "\n".join(
                [
                    " ".join(
                        [
                            f"{varnames[i][j]} = {solution[i][j]}"
                            for j in range(len(solution[0]))
                        ]
                    )
                    for i in range(len(solution))
                ]
            )
            oldWindow.write(self.text_output, result)
        except:
            oldWindow.write(self.text_output, "Invalid input")

    def init_trans(self):
        """inits trans part of the GUI"""
        self.kys()
        self.trans_is_init = True
        self.init_trans_b.configure(fg="green")
        self.basis_known_b = tk.Button(
            self.window,
            text="Basis known",
            command=self.init_trans_basis_known,
            fg="green",
        )
        self.basis_known_b.grid(row=0, column=1)
        self.basis_unknown_b = tk.Button(
            self.window, text="Points known", command=self.init_trans_basis_unknown
        )
        self.basis_unknown_b.grid(row=1, column=1)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=2)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input2.grid(row=1, column=3)
        self.text_input3 = tk.Text(self.window, height=10, width=30)
        self.text_input3.grid(row=1, column=4)
        self.text_output = tk.Text(self.window, height=10, width=30)
        self.text_output.grid(row=2, column=3)
        self.trans_label1 = tk.Label(self.window, text="First Basis:")
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(
            self.window, text="Vector in first basis:\n(Nothing for transition matrix)"
        )
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(self.window, text="Second Basis:")
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(self.window, text="Execute", command=self.exectrans)
        self.execute_b.grid(row=2, column=4)

    def init_trans_basis_unknown(self):
        """inits trans_buk subpart of trans GUI"""
        self.trans_label1.destroy()
        self.trans_label2.destroy()
        self.trans_label3.destroy()
        self.execute_b.destroy()
        self.basis_known_b.configure(fg="black")
        self.basis_unknown_b.configure(fg="green")
        self.trans_label1 = tk.Label(
            self.window, text="Known common points in basis 1:"
        )
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(
            self.window, text="Vector in first basis:\n(Nothing for transition matrix)"
        )
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(
            self.window, text="Known common points in basis 2:"
        )
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(
            self.window, text="Execute", command=self.execuktrans
        )
        self.execute_b.grid(row=2, column=4)

    def init_trans_basis_known(self):
        """inits trans_bk subpart of trans GUI"""
        self.trans_label1.destroy()
        self.trans_label2.destroy()
        self.trans_label3.destroy()
        self.execute_b.destroy()
        self.basis_known_b.configure(fg="green")
        self.basis_unknown_b.configure(fg="black")
        self.trans_label1 = tk.Label(self.window, text="First Basis:")
        self.trans_label1.grid(row=0, column=2)
        self.trans_label2 = tk.Label(self.window, text="Point in first CS:")
        self.trans_label2.grid(row=0, column=3)
        self.trans_label3 = tk.Label(self.window, text="Second Basis:")
        self.trans_label3.grid(row=0, column=4)
        self.execute_b = tk.Button(self.window, text="Execute", command=self.exectrans)
        self.execute_b.grid(row=2, column=4)

    def deinit_trans(self):
        """deinits trans part of the GUI"""
        if self.trans_is_init:
            self.trans_is_init = False
            self.init_trans_b.configure(fg="black")
            self.basis_known_b.destroy()
            self.basis_unknown_b.destroy()
            self.text_input1.destroy()
            self.text_input2.destroy()
            self.text_input3.destroy()
            self.text_output.destroy()
            self.trans_label1.destroy()
            self.trans_label2.destroy()
            self.trans_label3.destroy()
            self.execute_b.destroy()

    def exectrans(self):
        """Commences vector basis transition by calling Solver"""
        try:
            basis1 = Matrix(Matrix.read(self.text_input1.get("1.0", "end-1c")))
            veclst = self.text_input2.get("1.0", "end-1c").split()
            basis2 = Matrix(Matrix.read(self.text_input3.get("1.0", "end-1c")))
            self.solver.change_matrixa(basis1)
            self.solver.change_matrixb(basis2)
            if veclst == [] or veclst == [""]:
                oldWindow.write(self.text_output, self.solver.transmat().print())
            else:
                vector = Vector(veclst, basis1)
                self.solver.change_vectora(vector)
                oldWindow.write(self.text_output, self.solver.transvec().print())
        except Exception:
            oldWindow.write(self.text_output, "Invalid input")

    def execuktrans(self):
        """Commences Point coordinate system transition by calling solver"""
        try:
            self.solver.change_matrixa(
                Matrix(Matrix.read(self.text_input1.get("1.0", "end-1c")))
            )
            self.solver.change_vectora(
                Vector(self.text_input2.get("1.0", "end-1c").split())
            )
            self.solver.change_matrixb(
                Matrix(Matrix.read(self.text_input3.get("1.0", "end-1c")))
            )
            oldWindow.write(self.text_output, self.solver.transpoints().print())
        except Exception:
            oldWindow.write(self.text_output, "Invalid input")

    def init_vecari(self):
        self.kys()
        self.vecari_is_init = True
        self.init_vecari_b.configure(fg="green")
        vecari_explanation = """        Middle inputs:
        '+' for addition
        '-' for subtraction
        '*' or '()' for scalar product
        '[]' for vector product
        '/' for vector division (TBA)
        for vector product of 3+ vectors,
        please convert them to the same
        basis and write them as columns
        under 'Vector 1 (a column)'
        """
        self.label1 = tk.Label(self.window, text="Basis of vector 1:")
        self.label2 = tk.Label(self.window, text="Vector 1 (a column):")
        self.label3 = tk.Label(self.window, text="Basis of vector 2:")
        self.label4 = tk.Label(self.window, text="Vector 2 (a column):")
        self.label5 = tk.Label(self.window, text="Basis of answer:")
        self.label6 = tk.Label(self.window, text="Answer:")
        self.label7 = tk.Label(self.window, text=vecari_explanation)
        self.label1.grid(row=0, column=1)
        self.label2.grid(row=0, column=2)
        self.label3.grid(row=0, column=4)
        self.label4.grid(row=0, column=5)
        self.label5.grid(row=2, column=1)
        self.label6.grid(row=2, column=2)
        self.label7.grid(row=3, column=5)
        self.text_input1 = tk.Text(self.window, height=10, width=30)
        self.text_input2 = tk.Text(self.window, height=10, width=30)
        self.text_input3 = tk.Text(self.window, height=10, width=30)
        self.text_input4 = tk.Text(self.window, height=10, width=30)
        self.text_output1 = tk.Text(self.window, height=10, width=30)
        self.text_output2 = tk.Text(self.window, height=10, width=30)
        self.text_input1.grid(row=1, column=1)
        self.text_input2.grid(row=1, column=2)
        self.text_input3.grid(row=1, column=4)
        self.text_input4.grid(row=1, column=5)
        self.text_output1.grid(row=3, column=1)
        self.text_output2.grid(row=3, column=2)
        self.ari_input = tk.Entry(self.window, width=3)
        self.ari_input.grid(row=1, column=3)
        self.execute_b = tk.Button(
            self.window,
            text="Execute",
            command=self.exec_vecari,
            activebackground="green",
        )
        self.execute_b.grid(row=3, column=4)

    def deinit_vecari(self):
        if self.vecari_is_init:
            self.vecari_is_init = False
            self.init_vecari_b.configure(fg="black")
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.label4.destroy()
            self.label5.destroy()
            self.label6.destroy()
            self.label7.destroy()
            self.text_input1.destroy()
            self.text_input2.destroy()
            self.text_input3.destroy()
            self.text_input4.destroy()
            self.text_output1.destroy()
            self.text_output2.destroy()
            self.ari_input.destroy()
            self.execute_b.destroy()

    def exec_vecari(self):
        pass
