import numpy as np
import matplotlib.pyplot as plt
import sympy as sym



def _del2(p0, p1, d):
    return p0 - np.square(p1 - p0) / d

def _relerr(a, b):
    return (a - b) / b

def fixed_point(f,x0,method = 'del2'):
    p0 = x0
    for i in range(500):
        p1 = f(p0)
        use_accel = {'del2': True, 'iteration': False}[method]
        if use_accel:
            p2 = f(p1)
            d = p2-2.0*p1+p0
            p = _del2(p0, p1, d)
        else:
            p=p1
        relerr = _relerr(p, p0)
        if np.all(abs(relerr) < 1e-8):
            return p
        p0 = p

def newtonMethod(x0):

    if f_func(x0) == 0:
        return x0
    else:
        print(x0)
        return newtonMethod(np.float128(x0 - f_func(x0) / df_func(x0)))

def newtonMethod2(x0):

    if df_func(x0) == 0:
        return x0
    else:
        print(x0)
        return newtonMethod(np.float128(x0 - df_func(x0) / ddf_func(x0)))

def fixed_point(x):
    while True:
        xn = f_func(x)
        if(xn < 1.64548635):
            return x
        x = xn





# x = np.linspace(0, 6, num=1000)
# function = np.exp(x-np.pi)+np.cos(x)-x+np.pi
# plt.plot(x, function)
# plt.show()

x = sym.Symbol('x')
f = sym.exp(x-sym.pi)+sym.cos(x)-x+sym.pi

df = sym.diff(f, x)
ddf = sym.diff(df, x)

f_func = sym.lambdify(x, f, 'numpy')
df_func = sym.lambdify(x, df, 'numpy')
ddf_func = sym.lambdify(x, ddf, 'numpy')

print(fixed_point(1))




