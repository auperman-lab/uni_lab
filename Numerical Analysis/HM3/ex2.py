import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.special import gamma
from numpy import log, exp
from prettytable import PrettyTable

table = PrettyTable()


x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 1, 2, 6, 24])
y1 = np.array([0, 0, log(2), log(6), log(24)])


def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
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


x_new = np.arange(1, 5, 0.01)
a_s = divided_diff(x, y)[0, :]
a1_s = divided_diff(x, y1)[0, :]
y_new = newton_poly(a_s, x, x_new)
y1_new = newton_poly(a1_s, x, x_new)
table.field_names=['f(x)', 'D1(x)', 'D2(x)', 'D3(x)', 'D4(x)']
for row in divided_diff(x, y):
    table.add_row(row)
print(table)
f = CubicSpline(x, y, bc_type='natural')

maxnf = 0
maxnlf = 0
maxcs = 0
xxx = [x/100. for x in range(100, 500)]

for i in x_new:
    maxnf = max(maxnf, abs(gamma(i)-newton_poly(a_s, x, i)))
    maxnlf = max(maxnlf, abs(gamma(i)-exp(newton_poly(a1_s, x, i))))
    maxcs = max(maxcs, abs(gamma(i)-f(i)))

print('Newton formula max error: ', maxnf)
print('Newton formula for log(gamma) max error: ', maxnlf)
print('Cubic Spline max error: ', maxcs)

plt.plot(x, y, 'bo')
plt.plot(x_new, y_new, 'r', label='Newton formula')
plt.plot(x_new, exp(y1_new), 'black', label='Newton formula for log(gamma) ')
plt.plot(x_new, f(x_new), 'b', label='Cubic Spline')
plt.plot(x_new, gamma(x_new), 'g', label='Gamma Functio')
plt.legend()
plt.grid()
plt.show()