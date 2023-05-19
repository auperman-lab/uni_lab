from numpy import *


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
    if (n == 0):
        return x * 0
    elif (n == 1):
        return x * 0 + 1.0
    else:
        return (n / (x ** 2 - 1.0)) * (x * legendre(n, x) - legendre(n - 1, x))


def legendre_roots(polyorder, tolerance=1e-20):
    if polyorder < 2:
        err = 1  # bad polyorder no roots can be found
    else:
        roots = []
        # The polynomials are alternately even and odd functions. So we evaluate only half the number of roots.
        for i in range(1, int(polyorder / 2) + 1):
            x = cos(pi * (i - 0.25) / (polyorder + 0.5))
            error = 10 * tolerance
            iters = 0
            while (error > tolerance) and (iters < 1000):
                dx = -legendre(polyorder, x) / derivate_legendre(polyorder, x)
                x = x + dx
                iters = iters + 1
                error = abs(dx)
            roots.append(x)
        # Use symmetry to get the other roots
        roots = array(roots)
        if polyorder % 2 == 0:
            roots = concatenate((-1.0 * roots, roots[::-1]))
        else:
            roots = concatenate((-1.0 * roots, [0.0], roots[::-1]))
        err = 0  # successfully determined roots
    return roots, err


def gauss_legendre_weights(polyorder):
    W = []
    [xis, err] = legendre_roots(polyorder)
    if err == 0:
        W = 2.0 / ((1.0 - xis ** 2) * (derivate_legendre(polyorder, xis) ** 2))
        err = 0
    else:
        err = 1  # could not determine roots - so no weights
    return [W, xis, err]


def gauss_legendre_quad(func, polyorder, a, b):
    [Ws, xs, err] = gauss_legendre_weights(polyorder)
    if err == 0:
        ans = (b - a) * 0.5 * sum(Ws * func((b - a) * 0.5 * xs + (b + a) * 0.5))
    else:
        # (in case of error)
        err = 1
        ans = None
    return [ans, err]


def func(x):
    return exp(x)


order = 10
[Ws, xs, err] = gauss_legendre_weights(order)
if err == 0:
    print("Order    : ", order)
    print("Roots    : ", xs)
    print("Weights  : ", Ws)
else:
    print("Roots/Weights evaluation failed")

[ans, err] = gauss_legendre_quad(func, order, 0, 3)
if err == 0:
    print("Integral : ", ans)
else:
    print("Integral evaluation failed")
