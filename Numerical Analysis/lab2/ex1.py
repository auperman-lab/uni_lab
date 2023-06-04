from numpy import *
import sympy as sp


def legendre(n, x):
    x = array(x)
    if n == 0:
        return x * 0 + 1.0
    elif n == 1:
        return x
    else:
        return ((2.0 * n - 1.0) * x * legendre(n - 1, x) - (n - 1) * legendre(n - 2, x)) / n


def derivate_legendre(n, x):
    x = array(x)
    if n == 0:
        return x * 0
    elif n == 1:
        return x * 0 + 1.0
    else:
        return (n / (x ** 2 - 1.0)) * (x * legendre(n, x) - legendre(n - 1, x))


def legendre_roots(polyorder, tolerance):
    roots = []
    for i in range(1, int(polyorder / 2) + 1):
        x = cos(pi * (i - 0.25) / (polyorder + 0.5))
        error = 10 * tolerance
        iters = 0
        while error > tolerance:
            dx = -legendre(polyorder, x) / derivate_legendre(polyorder, x)
            x = x + dx
            iters = iters + 1
            error = abs(dx)
        roots.append(x)
    roots = array(roots)
    if polyorder % 2 == 0:
        roots = concatenate((-1.0 * roots, roots[::-1]))
    else:
        roots = concatenate((-1.0 * roots, [0.0], roots[::-1]))
    return roots


def gauss_legendre_weights(polyorder, tol):
    xis = legendre_roots(polyorder, tol)

    W = 2.0 / ((1.0 - xis ** 2) * (derivate_legendre(polyorder, xis) ** 2))

    return W, xis


def gauss_legendre_quad(func, polyorder, a, b, tol):
    Ws, xs = gauss_legendre_weights(polyorder, tol)
    x1 = (b - a) * 0.5 * xs + (b + a) * 0.5
    ans = (b - a) * 0.5 * sum(Ws * [func.evalf(subs={x: i}) for i in x1])

    return ans


interval = list(map(int, input("Write the interval: ").split()))
x = sp.Symbol('x')
func = sp.sympify(input('Write the function(use x to denote variable please): '))
order = int(input('Write how many roots : '))
tolerance = float(input('Write the precision : '))

Ws, xs = gauss_legendre_weights(order, tolerance)

ans = gauss_legendre_quad(func, order, interval[0], interval[1], tolerance)

print("Roots    : ", xs)
print("Weights  : ", Ws)
print("Integral : ", ans)
