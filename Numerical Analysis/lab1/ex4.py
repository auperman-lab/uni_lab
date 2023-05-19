import numpy as np
import sympy as sp
from prettytable import PrettyTable


def one_iteration(f, x, x0):
    n = len(f)
    m = len(x)
    values = {x[i]: x0[i] for i in range(m)}
    jac = sp.Matrix(f).jacobian(x)
    dx = jac.inv()*sp.Matrix(f)
    return np.array([-i.subs(values) for i in dx]).astype(float)


def newton_rapson_method(f, x, x0, err):
    errors = [1]
    xtable = np.array([x0])
    i = 0
    while errors[i] > err:
        deltax = one_iteration(f, x, xtable[i])
        y = xtable[i]+deltax
        xtable = np.vstack((xtable, y))
        errors.append(np.linalg.norm(xtable[i+1] - xtable[i]) / np.linalg.norm(xtable[i+1]))
        i += 1
    print_results(xtable, x, errors)


def print_results(xtable, x, err_table):
    table = PrettyTable()
    table.field_names = [str(i) for i in x]
    table.add_rows([[i for i in j] for j in xtable])
    table.add_column("Error", err_table)
    print(table)


x = list(map(str, input("Write the Symbols: ").split()))
x = [sp.symbols(i) for i in x]
x0 = list(map(int, input("Write the Initial Guess: ").split()))
f = list(map(sp.sympify, input("Write the Functions: ").split()))

# x1, x2, x3 = sp.symbols("x1 x2 x3")
# x = [x1, x2, x3]
# x0 = [1, 1, 1]
# f = [x[0]**2 + x[1]**2 - x[2]**2 - 3*x[0] - 3*x[1] - 3*x[2] + 6,
#      x[0]**2 + x[1]**2 - x[2]**2 - 2*x[0] - 2*x[1] - 2*x[2] + 3,
#      x[1]**2 + x[2]**2 - x[0]**2 - 2*x[0] - 2*x[1] - 2*x[2] + 3]

newton_rapson_method(f, x, x0, 10 ** (-8))
print("\n", sp.nsolve(f, x, x0))



