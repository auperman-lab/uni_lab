from numpy import cos, pi, sqrt, linspace, array, arange, zeros
import matplotlib.pyplot as plt


def divided_diff(x, y):
    n = len(y)
    coef = zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef


def newton_poly(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


f = lambda x: sqrt(x+1)

i = array(range(7))
chebyshevroots = cos((2*i+1)*pi/14)

x = linspace(-1, 1, 7)
y = [f(i) for i in x]

y_cheb = [f(i) for i in chebyshevroots]

x_new = arange(-1, 1, 0.01)
a_s = divided_diff(x, y)[0, :]
a_scheb = divided_diff(chebyshevroots, y_cheb)[0, :]
p7 = newton_poly(a_s, x, x_new)
m7 = newton_poly(a_scheb, chebyshevroots, x_new)


plt.plot(x_new, p7, 'r', label='Newton Method')
plt.plot(x_new, m7, 'b', label='Chebyshev lagrange')
plt.plot(x_new, f(x_new), 'black', label='Original function')
plt.plot(x, y, 'ro')
plt.plot(chebyshevroots, y_cheb, 'bo')
plt.legend()
plt.grid()
plt.show()
