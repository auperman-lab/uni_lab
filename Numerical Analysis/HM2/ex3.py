from sympy import *
import numpy as np


def newton(f, df, x0, tol, t):
    if abs(x0-t) < tol:
        return t
    else:
        t = x0
        return newton(f, df, x0 - f(x0)/df(x0), tol, x0)


x = symbols('x')
f1_lambada = lambda x:1.129241*10**(-3)+2.341077*10**(-4)*np.log(x)+8.775468*10**(-8)*np.log(x)**3-1/(19.01+273.15)
f2_lambada = lambda x:1.129241*10**(-3)+2.341077*10**(-4)*np.log(x)+8.775468*10**(-8)*np.log(x)**3-1/(18.99+273.15)
df_lambada = lambda x: 2.6326404e-7*np.log(x)**2/x + 0.0002341077/x
print(newton(f1_lambada, df_lambada, 15000, 10**-5, 100))
print(newton(f2_lambada, df_lambada, 15000, 10**-5, 100))

