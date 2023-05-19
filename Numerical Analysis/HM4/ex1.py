from scipy.special import gamma
import scipy.integrate as integrate
from numpy import exp
from prettytable import PrettyTable
x = PrettyTable()



def f(t, i):
    return t**(i-1) * exp(-t)


def composite_simpson(f, a, b, n, i):
    h = (b-a)/n
    integral = f(a, i)
    for j in range(1, n):
        if j % 2 == 1:
            integral += 4*f(a+j*h, i)
        else:
            integral += 2*f(a+j*h, i)

    integral += f(b, i)
    integral *= h/3
    return integral


arr = []
for i in range(1, 11):
    arr.append(integrate.quad(lambda x: f(x, i), 0, 45)[0])

x.add_column('x', list(range(1, 11)))
x.add_column('Composite Simpson rule', [composite_simpson(f, 0, 50, 300, i) for i in range(1, 11)])
x.add_column('Quad Aproximation', arr)
x.add_column('Gamma Function', [gamma(i) for i in range(1, 11)])
print(x)
