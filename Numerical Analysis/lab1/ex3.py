from numpy import sqrt
from prettytable import PrettyTable
table = PrettyTable()


x1 = 0
x2 = 1
x3 = 2
err = 10**(-8)


def f(x):
    return x**3 + 2*x**2 + 10*x - 20


def muller(x1, x2, x3, i=4):
    q = (x3 - x2) / (x2 - x1)
    a = q * f(x3) - q * (1 + q) * f(x2) + q ** 2 * f(x1)
    b = (2 * q + 1) * f(x3) - (1 + q) ** 2 * f(x2) + q ** 2 * f(x1)
    c = (1 + q) * f(x3)

    root1 = x3 - (x3 - x2) * (2 * c / (b + sqrt(b ** 2 - 4 * a * c)))
    root2 = x3 - (x3 - x2) * (2 * c / (b - sqrt(b ** 2 - 4 * a * c)))

    if abs(f(root1)) < abs(f(root2)):
        x4 = root1
    else:
        x4 = root2

    if x4.imag == 0j:
        x4 = x4.real

    if abs(f(x4)) > err:
        table.add_row([i, x4, f(x4)])
        return muller(x2, x3, x4, i+1)


table.field_names = ["Iteration", "x", "f(x)"]
table.add_row([1, x1, f(x1)])
table.add_row([2, x2, f(x2)])
table.add_row([3, x3, f(x3)])

muller(x1, x2, x3)

print(table)
