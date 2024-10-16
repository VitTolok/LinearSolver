"""
Эта программа вычисляет детерминанты матриц и решает базовые системы линейных уравнений.
Система линейных уровнений должна иметь N уравнений и N неизвестных.
Пример работы №1:
in: 2                // Первая строчка - размерность матрицы или число уравнений (N)
    1 2              // Матрица размерности N*N, пострчно
    3 4
out: -> det = -2     // Результат - детерминант
Пример работы №2:
in: 2                // Кол-во уравнений и неизвестных
    1 1 5            // "х1 + х2 = 5"
    1 -1 1           // "х1 - х2 = 1"
out: -> x1 = 3.0     // Реультаты в понятном виде
out: -> x2 = 2.0

Интересные случаи
ошибка самого Питона - не знаю
invalid input - введена странная матрица с непостоянной длиной строки
no or inf - решения нет или их бесконечно много (который именно хз, зависит от уравнений)
nothing to solve - то и значит, "решать нечего"

От количества пробелов между числами поведение программы зависеть не должно.

Сделал по приколу :/

v2 - Добавлена возможность решения систем с несовпадающим числом неизвестных и уравнений
путём отбрасывания некоторых из них.
Не знаю, зачем.
Не спрашивай

"""

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    determ = 0
    for i in range(len(matrix)):
        determ += matrix[i][0] * ((-1)**i) * det([row[1:] for row in (matrix[:i]+matrix[i+1:])])
    return determ

def square_solve(matrix, var_names):
    delta = det([row[:-1] for row in matrix])
    if delta == 0:
        return ["no or inf"]
    solution = []
    for i in range(len(matrix)):
        solution.append(f"{var_names[i]} = {det([row[:i] + [row[-1]] + row[i + 1:-1] for row in matrix]) / delta}")
    return solution

def linear_solver(matrix, var_names=None, equation_numbers=None, depth=0):
    n = len(matrix)
    length = len(matrix[0])
    allsamelen = True
    for row in matrix:
        if len(row) != length:
            allsamelen = False
            break
    if not allsamelen:
        print(f"{'\t'*depth}invalid input")
        exit(0)
    if var_names == None:
        var_names=[]
        for i in range(1, length):
            var_names.append(f"x{i}")
    if equation_numbers == None:
        equation_numbers = []
        for i in range(1, length+1):
            equation_numbers.append(f"{i}")
    if length == n:
        print(f"{'\t'*depth}det = {det(matrix)}")
    if length < 2:
        print("nothing to solve")
        return None
    if length == n+1:
        print(f"{'\t'*depth}{f'\n{'\t'*depth}'.join(square_solve(matrix, var_names))}")
    if length > n+1:
        for i in range(length-1):
            print(f"{'\t'*depth}Assuming {var_names[i]} == 0:")
            linear_solver([row[:i]+row[i+1:] for row in matrix], var_names=var_names[:i]+var_names[i+1:],
                          equation_numbers=equation_numbers, depth=depth + 1)
    if length < n+1:
        for i in range(len(matrix)):
            print(f"{'\t'*depth}Discarding equation {i+1}:")
            linear_solver(matrix[:i]+matrix[i+1:], var_names=var_names,
                          equation_numbers=equation_numbers[:i]+equation_numbers[i+1:], depth=depth + 1)



n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
linear_solver(matrix)
