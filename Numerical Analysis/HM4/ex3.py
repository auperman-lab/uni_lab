from numpy import pi, cos, sin, linspace
import scipy.integrate as integrate
from scipy.special import fresnel
import matplotlib.pyplot as plt


def cf(x):
    return cos((pi*x**2)/2)


def sf(x):
    return sin((pi*x**2)/2)


def simpson(f, a, b, n):
    h = (a+b)/n
    integral = f(a)
    for j in range(1, n):
        if j % 2 == 1:
            integral += 4*f(a+j*h)
        else:
            integral += 2*f(a+j*h)

    integral += f(b)
    integral *= h/3
    return integral


y_myc = []
y_mys = []
y_quads = []
y_quadc = []
x_my = linspace(0, 10, 300)
for i in x_my:
    y_myc.append(simpson(cf, 0, i, 150))
    y_mys.append(simpson(sf, 0, i, 150))
    y_quads.append(integrate.quad(lambda x:sf(x), 0, i)[0])
    y_quadc.append(integrate.quad(lambda x:cf(x), 0, i)[0])

x = linspace(0, 10, 1000)
s, c = fresnel(x)


plt.plot(x_my, y_myc, label='My Fresnel C')
plt.plot(x_my, y_mys, label='My Fresnel S')
# plt.plot(x_my, y_quads, label='Quad Fresnel S')
# plt.plot(x_my, y_quadc, label='Quad Fresnel C')
plt.plot(x, s, label='Fresnel S')
plt.plot(x, c, label='Fresnel C')

plt.ylabel('Y')
plt.ylabel('X')
plt.legend()
plt.show()
