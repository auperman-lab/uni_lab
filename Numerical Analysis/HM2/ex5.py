from numpy import square,all,cos


f = lambda x: cos(x)-1+x

def fixed_point(x):
    while True:
        xn = f(x)
        if(xn < 10**-6):
            return x
        x = xn


def aitken_algorithm(x0):
    while True:
        x1 = f(x0)
        x2 = f(x1)
        lambd  = (x2-x1)/(x1-x0)

        x3 = x2+lambd*(x2-x1)/(1+lambd)
        if x3 < 10**-6:
            return x3
        else:
            print(x3)
            x0 = x3



print(aitken_algorithm(0.1))
