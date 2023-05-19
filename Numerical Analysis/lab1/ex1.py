from numpy import exp, sign

a = -2
b = 0
err = 10**-8


def f(x):
    return exp(x)-x**2


def bisection(a, b):
    c = (a+b)/2
    if abs((b-a)/2) <= err or c == 0:
        return print("interval is: [", a, ",", c, "]")

    if sign(f(c)) != sign(f(a)):
        print(a, c)
        bisection(a, c)
    else:
        print(c, b)
        bisection(c, b)


bisection(a, b)
