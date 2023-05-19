from numpy import pi
import scipy.integrate as integrate
import time
from prettytable import PrettyTable
table1 = PrettyTable()


def f(x):
    return 4/(1+x**2)


def simpson(f, a, b, n):
    h = (b-a)/n
    integral = f(a)
    for j in range(1, n):
        if j % 2 == 1:
            integral += 4*f(a+j*h)
        else:
            integral += 2*f(a+j*h)

    integral += f(b)
    integral *= h/3
    return integral
def trapezoidal(f, a, b, n):
    h = (b-a)/n
    integral = f(a)
    for j in range(1, n):
        integral += 2*f(a+j*h)
    integral += f(b)
    integral *= h/2
    return integral


def midpoint(f, a, b, n):
    h = (b-a)/n
    integral = 0
    for j in range(n+1):
        integral += h*f(a+j*h)
    return integral

arr2 = []
arr3 = ['-']
arr4 = ['-', '-']
for i in range(4, 14):
    arr2.append(simpson(f, 0, 1, 2**i))
for i in range(1, len(arr2)):
    arr3.append(arr2[i]-arr2[i-1])
for i in range(2, len(arr3)):
    if arr3[i] != 0:
        arr4.append(arr3[i-1]/arr3[i])
    else:
        arr4.append('-')
table1.add_column('Roots', [2**i for i in range(4, 14)])
table1.add_column('I(n)', arr2)
table1.add_column('I(n)-I(n-1)', arr3)
table1.add_column('Ratio', arr4)
table1.add_column('Absolute Error', [pi-i for i in arr2])
print(table1.get_string(title="Composite Simpson's Rule"))
table1.clear()

arr2 = []
arr3 = ['-']
arr4 = ['-', '-']
for i in range(16, 24):
    arr2.append(midpoint(f, 0, 1, 2**i))
for i in range(1, len(arr2)):
    arr3.append(arr2[i]-arr2[i-1])
for i in range(2, len(arr3)):
    arr4.append(arr3[i-1]/arr3[i])
table1.add_column('Roots', [2**i for i in range(16, 24)])
table1.add_column('I(n)', arr2)
table1.add_column('I(n)-I(n-1)', arr3)
table1.add_column('Ratio', arr4)
table1.add_column('Absolute Error', [pi-i for i in arr2])
print(table1.get_string(title="Composite Midpoint Rule"))


start = time.time()
simpson(f, 0, 1, 500)
final = time.time()
print('time for simpson method :', final-start, '\n')

start = time.time()
print('error for quad aproximation :', integrate.quad(lambda x: f(x), 0, 1, epsrel=1.49e-1)[0]-pi, '\n')
final = time.time()
print('time for quad :', final-start)
