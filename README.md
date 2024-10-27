# LinearSolver


- [LinearSolver](#linearsolver)
  - [Overview](#overview)
  - [LinearSolver's Dependencies](#linearsolvers-dependencies)
  - [How to run](#how-to-run)
  - [General Structure](#general-structure)
    - [main.py](#mainpy)
      - [Dependencies](#dependencies)
    - [Window.py](#windowpy)
      - [Dependencies](#dependencies-1)
    - [Solver.py](#solverpy)
      - [class Solver](#class-solver)
      - [class LinSolver](#class-linsolver)
      - [class MatDivSolver](#class-matdivsolver)
      - [class TransBasisSolver](#class-transbasissolver)
      - [class TransCoordSolver](#class-transcoordsolver)
      - [class VecAriSolver](#class-vecarisolver)
      - [Dependencies](#dependencies-2)
    - [Matrix.py](#matrixpy)
    - [Vector.py](#vectorpy)
      - [Dependencies](#dependencies-3)
  - [GUI](#gui)


## Overview

This project is a simple program built with the purpose of assisting the user in Calcultion, related to matrixes, such as: determinator calculation, matrix arithmetics, system of linear equations solution, basis and coodinate system transition and more (possibly in the future)

It was made entirely by me, @VitTolok.

## LinearSolver's Dependencies

This project (apart from standard python) only depends on one library, ***tkinter***, which is used for creating GUI

## How to run

If not already installed, install tkinter:
```
pip install tkinter
```
Run main.py:
```
python3 main.py
```

## General Structure

The functionality of this program is split into several parts:
- main.py
- Window.py
- Solver.py
- Classes folder

### main.py

This is the file for launching the program, by itself it does not do anything useful, it just creates a Window object that will manage the rest of the functionality and user interaction going forward.

#### Dependencies

Internal:
- the Window class from Window.py

### Window.py
The Window.py file contains one class called "Window"

A Window object is responsible for maintaining the GUI, it creates and deletes different parts of the GUI when necessary, reads user input, coverts it for it to be processed elsewhere, retrieves it and converts back to user readable text.

Once a Window object has been created, the basic GUI appears on screen and the program enters the main loop, which it does not leave until the window is closed or the program is stopped forcefully. The only exception is when a button is pressed in the GUI, which calls for one of the Window object's own methods responsible for that button's functionality.

This Class is not for general use as it is entirely hardcoded to maintain this specific project.

#### Dependencies

Internal:
- All of the Solver classes
- The Classes folder files

External:

- tkinter, a GUI library that is bundled with python

### Solver.py

This Python file contains classes for data processing, each class containing some section of the program's useful functionality
The list of Solver classes may not be final.

#### class Solver

Basic senior abstract class containing basic data input handling

- ***\_\_init__(input_list)*** - the constructor, writes down the input data list
- **.setinput(value, index)** - change the object with given index in the input data list to the given one
- **.getinput(index)** - returns the object with given index in the input data list
- **.get_solution()** - returns the solution, defined by non-abstract child classes

#### class LinSolver

A class for solving Linear equations defined by AX=B, where A and B are given Matrixes, child of [Solver](#class-solver)

- **._linsolve(a, b)** - returns the X matrix, assuming Matrixes A and B have indexes a and b respectfully in the input data list
- **.get_solution()** - calls for ***._linsolve(0, 1)***

#### class MatDivSolver
A class for performing matrix division by inverted matrix multiplication. Only accepts square matrixes as divisors. Child of [LinSolver](#class-linsolver)

- **._matdiv(a, b)** - returns the result of dividing Matrix A by Matrix B, assuming Matrixes A and B have indexes a and b respectfully in the input data list. Performs calculations using ***._linsolve*** from parent [LinSolver](#class-linsolver)
- **.get_solution()** - calls for ***._matdiv(0, 1)***

#### class TransBasisSolver
A class that creates, stores and applies a basis transition matrix for vectors. Child of [LinSolver](#class-linsolver)

- ***\_\_init__(input_list)*** - the modified constructor. Additionally calculates and writes down the transition matrix, assuming the basis vectors are stored as two matrixes under indexes 0 and 1
- **.transmat(initindex, tragetindex)** - calculates a transition matrix for Matrixes from data input list under indexes initindex and targetindex
- **.transvec(vector)** - returns given vector (or a batch of vectors as a matrix) in the target basis, assuming they were in the initial basis
- **.revertvec(vector)** - returns given vector (or a batch of vectors as a matrix) in the initial basis, assuming they were in the target basis
- **.get_solution()** - returns the transition matrix

#### class TransCoordSolver
Calculates and stores key points and a transition Matrix between two general Cartesian coordinate systems, given their common points. Child of [TransBasisSolver](#class-transbasissolver)

- ***\_\_init__(input_list)*** - the modified constructor. Additionally calculates and writes down the transition matrix and one key poin for each system, assuming the common points are stored as two matrixes under indexes 0 and 1
- **.transpoint(point)** - for a point Vector (or a batch stored as columns in a Matrix) in initial coordinate system, returns it in the target coordinate system
- **.revertpoint(point)** - for a point Vector (or a batch stored as columns in a Matrix) in target coordinate system, returns it in the initial coordinate system
- **.get_solution()** - returns the transition matrix

#### class VecAriSolver
Accepts two vectors with their basises and performs arithmetical operations with them. Also Supports Batches of Vectors in the same basis. Child of [TransBasisSolver](#class-transbasissolver)
- ***.\_\_init__(input_list)*** - writes down two vectors (indexes 1 and 3) and their basises, makes a transition matrix.
- **.add(basis)** - returns a Vector sum in a basis that depends on the *basis* integer input: 0 - unit orthogonal basis; 1 - first vector/batch's basis; 2 - second's
- **.sub(basis)** - returns a Vector subtraction result in a basis that depends on the *basis* integer input: 0 - unit orthogonal basis; 1 - first vector/batch's basis; 2 - second's
- **.scalmult()** - returns a complex number - the result of scalar multiplication
- **.vectmult(basis)** - returns a Vector multiplication result in a basis that depends on the *basis* integer input: 0 - unit orthogonal basis; 1 - first vector/batch's basis; 2 - second's. If there are more than 2 vectors to multiply, they must all be in the first batch.
#### Dependencies
Internal:
- Matrix from Matrix.py
- Vector from Vector.py

### Matrix.py
Contains one class, Matrix, resposible for storing Matrixes and conducting simple operations with them.
### Vector.py
Contains one class, Vector, resposible for storing Vectors and conducting simple operations with them.
#### Dependencies
Internal
- Matrix class from Matrix.py
## GUI
The main interface is separated into several categories, i.e. determinator, matrix arithmetics, etc. Each of them is accessed by pressing the corresponding button on the left. All of them require inputs from rhe user via text, the general rules to formatting the input of a matrix are:
- Separate rows of the matrix must be written on separate lines
- All elements of the same row must be on the same line
- Between two elements of the same row there must be at least one space (' ')
- Within one element there can be no spaces
- Integers can be written as follows: 123 -45
- Floats can be written like this: 1.23 -4.5
- Complex numbers like this: 1.2-3.4j -5.67+9j

For arithmetics categories put the corresponding operator in the middle, between the operands, be that vectors or matrixes

To get the result, press the 'Execute' button.