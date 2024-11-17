# LinearSolver

- [LinearSolver](#linearsolver)
  - [Overview](#overview)
  - [LinearSolver's Dependencies](#linearsolvers-dependencies)
  - [How to run](#how-to-run)
  - [General Structure](#general-structure)
    - [Classes](#classes)
      - [Matrix](#matrix)
      - [Vector](#vector)
    - [GUI](#gui)
      - [Window](#window)
      - [SubGUI](#subgui)
        - [SubGUI module](#subgui-module)
        - [TransitionSolverGUI](#transitionsolvergui)
          - [TransitionSolverGUI module](#transitionsolvergui-module)
          - [BasisTransitionGUI](#basistransitiongui)
          - [CoordinateTransitionGUI](#coordinatetransitiongui)
        - [DeterminatorGUI](#determinatorgui)
        - [LinearSolverGUI](#linearsolvergui)
        - [MatrixArithmeticsGUI](#matrixarithmeticsgui)
        - [MatrixGeneratorGUI](#matrixgeneratorgui)
        - [VectorArithmeticsGUI](#vectorarithmeticsgui)
      - [Input](#input)
        - [InputTable](#inputtable)
        - [InputField](#inputfield)
        - [BasisTransitionInput](#basistransitioninput)
        - [CoordinateTransitionInput](#coordinatetransitioninput)
        - [DeterminatorInput](#determinatorinput)
        - [LinearSolverInput](#linearsolverinput)
        - [MatrixArithmeticsInput](#matrixarithmeticsinput)
        - [VectorArithmeticsInput](#vectorarithmeticsinput)
    - [Solver](#solver)
      - [Solver module](#solver-module)
      - [BasisTransitionSolver](#basistransitionsolver)
      - [CoordinateTransitionSolver](#coordinatetransitionsolver)
      - [LinearSolver module](#linearsolver-module)
      - [MatrixDivisionSolver](#matrixdivisionsolver)
      - [VectorArithmeticsSolver](#vectorarithmeticssolver)

## Overview

This project is a simple program built with the purpose of assisting the user in Calcultion, related to matrixes, such as: determinator calculation, matrix arithmetics, system of linear equations solution, basis and coodinate system transition, vector arithmetics and more (possibly in the future)

It was made entirely by me, @VitTolok. Yes, believe me or not, not a single line of this project was written by anything but me, not even GPT had a hand in this.

## LinearSolver's Dependencies

This project (apart from standard python) only depends on one library, ***tkinter***, which is used for creating GUI

Also uses standard ***math*** library to enable the user to write complicated expressions as input.

## How to run

If not already installed, install tkinter:
```
pip3 install tkinter
```
Run main.py:
```
python3 src/main.py
```

## General Structure

The functionality of this program is split into several packages:
- [Classes](#classes)
- [GUI](#gui)
- [Solver](#Solver)

The contents of these packages are described below

### Classes

This package contains two modules:
- Matrix.py defining the [Matrix](#matrix) class
- Vector.py defining the [Vector](#vector) class

#### Matrix
An object of this class represents a matrix, and through this object the user can interact with it. Some Notable methods are:
- *\_\_init__(array_2d: list, skip_det = False)* - uses a list representing a matrix to construct one. the *skip_det* parameters allows the user to skip calculation of the determinator if it is not necessary even if the matrix is square.
- *e(size: int) -> Matrix* - a function that returns an eye matrix of the requested size
- *read(string: str, evaluate: bool = True) -> list\[list\[complex | str\]\]* - returns a list representation of a matrix, defined by its text form, given in *string*. the *evaluate* parameter defines whether the function will evaluate expressions into complex numbers or not.
- *.tolist() -> list\[list\[complex\]\]* - a method that turns the matrix back into its list representation.
- *.columns() -> list\[list\[complex\]\]* - a method that returns a list containing list representations of this matrix's columns
- *.rows() -> int* - the number of rows in this matrix
- *.cols() -> int* - the number of columns
- *.get(row: int, column: int) -> complex* - the value in the cell that lies in the given row and the given column.
- *.set(row: int, column: int, value: complex)* - sets the desired cell to a new value
- *.transposed()* - returns the transposed version of this matrix. Skips determinator calculation.
- *.is_square() -> bool* - whether this matrix is a square
- *.copy()* - returns a copy of this matrix
- *.det(recalculate: bool = False) -> complex | None* - returns the value of the determinator, if it exists and was already calculated, if *recalculate* is given as True, will attempt to recalculate the determinator (useful if it wasn't yet calculated or the matrix was changed)
- *.\_\_add__(other: Matrix) -> Matrix* - matrix addition (overloads '+' operator)
- *.\_\_sub__(other: Matrix) -> Matrix* - matrix subtraction (overloads '-' operator)
- *.\_\_mul__(other: Matrix | complex) -> Matrix* - matrix multiplication (overloads '*' operator), if *other* is a number, multiplies all elements by it.
- *.\_\_eq__(other: Matrix) -> bool* - whether the matrixes have all the same elements. '=='
- similarly working overloads of '+=' and '-='
- *.print() -> str* - returns this matrix as formatted text.
- *.\_\_len__() -> int* - overloads len() fulction, same as *.rows()*
- *clear_detcache()* - since calculating determinator is an N! algorithm, I added caching of already calculated ones to speed up the process, in extreme cases it may take up too much memory, so it has to be cleared from time to time.
- *sizeof_detcache()* - returns the size of the cache in bytes 

#### Vector
An object of this class represents a vector. Keeps its coordinates and the basis as well as its basis, in this project often sidelined, as a lot of it can be replaced with matrixes if you know what you're doing.
Depends on [Matrix](#matrix)

### GUI
Contains all objects that handle the GUI.
This package contains a module [Window](#window) as well as two packages:
- [Input](#input)
- [SubGUI](#subgui)

#### Window
This module defines one class to rule them all, a Window object creates a new Window, some basic buttons representing different parts of the GUI, as well as [SubGUI](#SubGUI) objects tied to these buttons that will handle what each of these parts actually does.
Depends on every [SubGUI](#SubGUI) module as well as ***tkinter***

#### SubGUI
this package contains:
- [SubGUI](#subgui-module) module
- [TransitionSolverGUI](#transitionsolvergui) package
- [DeterminatorGUI](#determinatorgui) module
- [LinearSolverGUI](#linearsolvergui) module
- [MatrixArithmeticsGUI](#matrixarithmeticsgui) module
- [MatrixGeneratorGUI](#matrixgeneratorgui) module
- [VectorArithmeticsGUI](#vectorarithmeticsgui) module

##### SubGUI module
This is an abstract class that handles basic logic for a part of the GUI

Every module in the [SubGUI](#subgui) package is a class that inherits from this one. Every child of this class has 3 main methods:
- *.activate()* - creates and displays all widgets that this part of the GUI requires.
- *.collapse()* - gets rid of all widgets created by *.activate()*
- *._calculate()* - this method is the one the execute button is supposed to call. Calculates the desired solution  and displays it on screen.

Depends on ***tkinter***

##### TransitionSolverGUI
This package contains three modules:
- [TransitionSolverGUI](#transitionsolvergui-module)
- [BasisTransitionGUI](#basistransitiongui)
- [CoordinateTransitionGUI](#coordinatetransitiongui)

###### TransitionSolverGUI module
This module is a child of [SubGUI](#subgui-module) that manages two other SubGUI's, since 
[BasisTransitionGUI](#basistransitiongui) and [CoordinateTransitionGUI](#coordinatetransitiongui) are so similar, they have their own subdivision.

Depends on [SubGUI](#subgui-module), [BasisTransitionGUI](#basistransitiongui) and [CoordinateTransitionGUI](#coordinatetransitiongui) as well as ***tkinter***

###### BasisTransitionGUI
This module handles basis transitions GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [BasisTransitionInput](#basistransitioninput) module, [Matrix](#matrix) module and [BasisTransitionSolver](#basistransitionsolver) module as well as ***tkinter***

###### CoordinateTransitionGUI
This module handles coordinate system transitions GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [CoordinateTransitionInput](#coordinatetransitioninput) module, [Matrix](#matrix) module and [CoordinateTransitionSolver](#coordinatetransitionsolver) module as well as ***tkinter***

##### DeterminatorGUI
This module handles the determinator calculation part of the GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [DeterminatorInput](#determinatorinput) module and [Matrix](#matrix) module, as well as ***tkinter***

##### LinearSolverGUI
This module handles linear equations GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [LinearSolverInput](#linearsolverinput) module, [Matrix](#matrix) module and [LinearSolver](#linearsolver) module as well as ***tkinter***

##### MatrixArithmeticsGUI
This module handles matrix arithmetics GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [MatrixArithmeticsInput](#matrixarithmeticsinput) module, [Matrix](#matrix) module and [MatrixDivisionSolver](#matrixdivisionsolver) module as well as ***tkinter***

##### MatrixGeneratorGUI
This module handles the matrix generator GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module) and [Matrix](#matrix) module as well as ***tkinter***

##### VectorArithmeticsGUI
This module handles vector arithmetics GUI. Child of [SubGUI](#subgui-module).

Depends on [SubGUI](#subgui-module), [VectorArithmeticsInput](#vectorarithmeticsinput) module, [Matrix](#matrix) module and [VectorArithmeticsSolver](#vectorarithmeticssolver) module as well as ***tkinter***

#### Input
The modules in this package are used by SubGUI's to handle switching between two input modes: text and table
this Package contains modules:
- [InputTable](#inputtable) 
- [InputField](#inputfield)
- [BasisTransitionInput](#basistransitioninput)
- [CoordinateTransitionInput](#coordinatetransitioninput)
- [DeterminatorInput](#determinatorinput)
- [LinearSolverInput](#linearsolverinput)
- [MatrixArithmeticsInput](#matrixarithmeticsinput)
- [VectorArithmeticsInput](#vectorarithmeticsinput)

##### InputTable
This module defines a class that handles creating and interacting with a rectangular table of entry widgets.
Its methods include:
- *.\_\_init__(master, rows: int, columns: int, buffer: str | None = None))* - basic setup for the creation of the table. Uses *buffer* to fill the table
- *.activate(row: int, column: int)* - displays the table at the desired grid cell inside the *master* window
- *.read()* - returns the collective input as text
- *.collapse()* - gets rid of the displayed table.

Depends on the [Matrix](#matrix) module as well as ***tkinter***

##### InputField
A parent class for all modules whose name ends in "Input". Defines basic logic for input type switching.
Its methods include:
- *.\_\_init__(master, switch_button: tk.Button)* - basic setup. Uses *switch_button* to set up the switch trigger
- *.activate(buffers: list\[str])* - activates text input and fills it using buffers
- *.collapse()* - collapses all inputs
- *.read(field: int = 0) -> str* - reads text from the desired input.

Some of these methods are universal for all descendants and thus are only defined here.

depends on ***tkinter***

##### BasisTransitionInput
Manages 3 fields for [BasisTransitionGUI](#basistransitiongui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

##### CoordinateTransitionInput
Manages 3 fields for [CoordinateTransitionGUI](#coordinatetransitiongui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

##### DeterminatorInput
Manages 1 field for [DeterminatorGUI](#determinatorgui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

##### LinearSolverInput
Manages 3 fields for [LinearSolverGUI](#linearsolvergui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

##### MatrixArithmeticsInput
Manages 2 fields for [MatrixArithmeticsGUI](#matrixarithmeticsgui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

##### VectorArithmeticsInput
Manages 4 fields for [VectorArithmeticsGUI](#vectorarithmeticsgui), child of [InputField](#inputfield)

Depends on [InputField](#inputfield), [InputTable](#inputtable) and the [Matrix](#matrix) module as well as ***tkinter***

### Solver
This package contains modules that exist to conduct complex calculations through creation of [Solver](#solver-module) objects. This package contains modules:
- [Solver](#solver-module)
- [BasisTransitionSolver](#basistransitionsolver)
- [CoordinateTransitionSolver](#coordinatetransitionsolver)
- [LinearSolver](#linearsolver-module)
- [MatrixDivisionSolver](#matrixdivisionsolver)
- [VectorArithmeticsSolver](#vectorarithmeticssolver)

#### Solver module
This is an abstract class for Solver objects. By itself it does not accomplish or calculate anything. All other modules in the [Solver](#solver) package are this class's descendants.

Does not have dependencies

#### BasisTransitionSolver
This is a class for calculating transition matrixes between two basises. Child of [LinearSolver](#linearsolver-module). The *input_list* must consist of the first and the second basis. Introduces methods:
- *.transmat(initindex: int, targetindex: int)* - calculates the transition matrix from initial basis to the target basis assuming initindex and targetindex are their indexes in the *input_list*
- *.set_transition(initindex: int, targetindex: int)* - same but stes them internally for future reference
- *.transvec(vector: Vector | Matrix)* - uses stored transition matrix to change the basis of the given vector or batch of vectors
- *.revertvec(vector: Vector | Matrix)* - same, but changes the vector's basis back to the initial one
- *.get_solution()* - returns the stored transition matrix

Depends on the [LinearSolver](#linearsolver-module) module, the [Matrix](#matrix) module and the [Vector](#vector) module

#### CoordinateTransitionSolver
This is a class for transitions between two coordinate systems with known common points. Child of [BasisTransitionSolver](#basistransitionsolver). The *input_list* must consist of the first and the second coordinate system coordinates for the common points as Matrixes. Introduces methods:
- *.transpoint(vector: Vector | Matrix)* - transitions given points to target coordinate system
- *.revertpoint(vector: Vector | Matrix)* - transitions the points back to initial coordinate system

Depends on [BasisTransitionSolver](#basistransitionsolver) module, the [Matrix](#matrix) module and the [Vector](#vector) module

#### LinearSolver module
This is a class for calculating a matrix X such that A*X = B, with given square matrix A and some Matrix B.
Child of [Solver](#solver-module). The *input_list* must contain matrixes A and B. Introduces methods:
- *._linsolve(a: int, b: int)* - calculates matrix X assuming a and b are indexes of A and B
- *.get_solution()* - returns solution for a = 0 and b = 1

Depends on [Solver](#solver-module) module and the [Matrix](#matrix) module

#### MatrixDivisionSolver
This is a class for calculating matrix division by inverted matrix multiplication. Child of [LinearSolver](#linearsolver-module). The input list must contain the operands. Introduces methods:
- *._matdiv(a: int, b: int)* - returns the result of dividing Matrix a by Matrix B
- *.get_solution()* - returns the solution for a = 0 and b = 1

Depends on the [LinearSolver](#linearsolver-module) module and the [Matrix](#matrix) module

#### VectorArithmeticsSolver
This is a class for conducting arithmetic opreations with two batches of vectors with different basises.
Child of [BasisTransitionSolver](#basistransitionsolver). The input list must contain:
  - the basis of the first batch
  - the first batch
  - the basis of the second batch
  - the second batch
  
Introduces methods:
- *.add(basis: 0 | 1 | 2)* - returns the sum of given vectors in the desired basis
- *.sub(basis: 0 | 1 | 2)* - returns the sub of given vectors in the desired basis
- *.scalmult()* - calculates the scalar product of 2 vectors
- *.mixmult()* - calculates the mixed product of N N-dimensional vectors
- *.vectormult()* - calculates the vector product of N N-dimensional vectors returns it in eye basis.
