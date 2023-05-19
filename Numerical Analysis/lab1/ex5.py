from numpy import exp

a = -2
b = 0
err = 10**-8


def f(x):
    return exp(x)-x**2


def hybrid_secant_bisection_method(x0, x1, f, err=10**-8):
    fx0 = f(x0)
    fx1 = f(x1)
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

    if abs(x1-x0) <= err:
        return print(x1)

    if abs(x2 - x1) >= abs(x1 - x0):
        print(x1, (x0 + x1)/2)
        hybrid_secant_bisection_method(x1, (x0 + x1)/2, f)
    else:
        print(x1, x2)
        hybrid_secant_bisection_method(x1, x2, f)


hybrid_secant_bisection_method(a, b, f)
