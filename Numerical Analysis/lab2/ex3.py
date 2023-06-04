import csv
import matplotlib.pyplot as plt
from numpy import zeros
from scipy.interpolate import CubicSpline


def romberg(f, a, b, y, n):
    r = zeros((n+1, n+1))
    h = b - a
    r[0][0] = 0.5 * h * (y[0] + y[-1])

    pw2 = 1
    for i in range(1, n + 1):

        h = 0.5 * h

        summ = 0
        pw2 = 2 * pw2
        for k in range(1, pw2, 2):
            q = int(a + k * h)
            if f == 0:
                summ += f1(a + k * h)
            elif f == 1:
                # print(y[q], y[q+1], a+k*h, linear_interpolation(y[q], y[q+1], a + k * h, q, q+1))
                summ += linear_interpolation(y[q], y[q+1], a + k * h, q, q+1)
            elif f == 2:
                # print(y[q], y[q+1], a+k*h, lagrange_method([q, q+1], [y[q], y[q+1]], a + k * h))
                summ += lagrange_method([q, q+1], [y[q], y[q+1]], a + k * h)
            elif f == 3:
                # print(y[q], y[q+1], a+k*h, newton_poly(divided_diff([q, q+1], [y[q], y[q+1]])[0, :], [q, q+1], a + k * h))
                summ += newton_poly(divided_diff([q, q+1], [y[q], y[q+1]])[0, :], [q, q+1], a + k * h)

        r[i][0] = 0.5 * r[i-1][0] + summ * h

        pw4 = 1
        for j in range(1, i + 1):
            pw4 = 4 * pw4
            r[i][j] = r[i][j-1] + (r[i][j-1] - r[i-1][j-1]) / (pw4 - 1)

    return r


def linear_interpolation(y0, y1, xp, x0, x1):
    return y0 + ((y1-y0)/(x1-x0)) * (xp - x0)


def lagrange_method(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j]) / (x[i] - x[j])

        yp = yp + p * y[i]
    return yp


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


x, y = [], []
x_spl, y_spl = [], []

with open('dataset_3.csv', 'r') as csv_file:
    file = csv.DictReader(csv_file)
    line_count = 0
    for row in file:

        x.append(int(row['Number of Items Purchased']))
        if row[' Time Spent (minutes)'] == ' Nan':
            y.append(0)
        else:
            y.append(int(row[' Time Spent (minutes)']))

y_lag = y_new = y_lin = [i for i in y]
for i in range(len(y)):
    if y[i] == 0:
        xa = [x[i-2], x[i-1], x[i+1], x[i+2]]
        ya = [y[i-2], y[i-1], y[i+1], y[i+2]]
        y_lag[i] = lagrange_method(xa, ya, x[i])
        y_new[i] = newton_poly(divided_diff(xa, ya)[0, :], xa, x[i])
        y_lin[i] = linear_interpolation(y[i-1], y[i+1], x[i], x[i-1], x[i+1])
    else:
        x_spl.append(x[i])
        y_spl.append(y[i])


f1 = CubicSpline(x_spl, y_spl)


print('integral on cubic spline', romberg(0, x[0], x[-1], y_lin, 3)[-1][-1])
print('integral on linear method', romberg(1, x[0], x[-1], y_lin, 3)[-1][-1])
print('integral on lagrange method', romberg(2, x[0], x[-1], y_lin, 3)[-1][-1])
print('integral on newton method', romberg(3, x[0], x[-1], y_lin, 5)[-1][-1])


# plt.plot(x, f1(x), 'r', label='cubic spline method')
# plt.plot(x, y_lag, 'b', label='lagrage method')
# plt.plot(x, y_lag, 'r', label='linear method')
plt.plot(x, y_new, 'r', label='newton method')
plt.plot(x, y, 'b', label='original function')
plt.show()
