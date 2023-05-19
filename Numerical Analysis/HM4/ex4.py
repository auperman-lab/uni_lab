from scipy.special import roots_legendre
import scipy.integrate as integrate
from prettytable import PrettyTable
table1 = PrettyTable()
table2 = PrettyTable()
a = 1
b = 5


def f(x):
    return 1/((x-1)**(5/2))


def t(t):
    return (a+b+t*(b-a))/2


def simpson(f, a, b, n):
    h = (b-a)/n
    integral = 0
    for j in range(1, n):
        if j % 2 == 1:
            integral += 4*f(a+j*h)
        else:
            integral += 2*f(a+j*h)

    integral += f(b)
    integral *= h/3
    return integral

arr1 = []
tegration = 0
for i in range(2, 7):
    x, w = roots_legendre(2**i)
    for j in range(2**i):
        tegration += w[j]*f(t(x[j]))
    tegration *= (b-a)/2
    arr1.append(tegration)
table2.add_column('Roots', [2**i for i in range(2, 7)])
table2.add_column('Gaussian quadrature DIY',arr1)


arr2 = []
arr3 = ['-']
arr4 = ['-', '-']
for i in range(2, 7):
    arr2.append(simpson(f, 1, 5, 2**i))
for i in range(1, len(arr2)):
    arr3.append(arr2[i]-arr2[i-1])
for i in range(2, len(arr3)):
    arr4.append(arr3[i-1]/arr3[i])
table1.add_column('Roots', [2**i for i in range(2, 7)])
table1.add_column('I(n)', arr2)
table1.add_column('I(n)-I(n/2)', arr3)
table1.add_column('Ratio', arr4)

print(table2)
print(table1.get_string(title="Composite Simpson's Rule"))

print('Build in function result: ', integrate.quad(f, a, b)[0])
