import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def lagrange_method(x, y, xp):
    n = 6
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j]) / (x[i] - x[j])

        yp = yp + p * y[i]
    return yp



xa = [2.1, 4.6, 5.25, 7.82, 9.2, 10.6]
ya = [7.3, 7.0, 6.0, 5.1, 3.5, 5.0]

x_ew = np.linspace(2, 11, 1000)

# l0 = lambda x: ya[0]*(x-xa[1])*(x-xa[2])*(x-xa[3])*(x-xa[4])*(x-xa[5]))/\
#                ((xa[0]-xa[1])*(xa[0]-xa[2])*(xa[0]-xa[3])*(xa[0]-xa[4])*(xa[0]-xa[5]))
#
# l1 = lambda x: ya[1]*((x-xa[0])*(x-xa[2])*(x-xa[3])*(x-xa[4])*(x-xa[5]))/\
#                ((xa[1]-xa[0])*(xa[1]-xa[2])*(xa[1]-xa[3])*(xa[1]-xa[4])*(xa[1]-xa[5]))
#
# l2 = lambda x: ya[2]*((x-xa[0])*(x-xa[1])*(x-xa[3])*(x-xa[4])*(x-xa[5]))/\
#                ((xa[2]-xa[1])*(xa[2]-xa[0])*(xa[2]-xa[3])*(xa[2]-xa[4])*(xa[2]-xa[5]))
#
# l3 = lambda x: ya[3]*((x-xa[0])*(x-xa[1])*(x-xa[2])*(x-xa[4])*(x-xa[5]))/\
#                ((xa[3]-xa[1])*(xa[3]-xa[2])*(xa[3]-xa[0])*(xa[3]-xa[4])*(xa[3]-xa[5]))
#
# l4 = lambda x: ya[4]*((x-xa[0])*(x-xa[1])*(x-xa[2])*(x-xa[3])*(x-xa[5]))/\
#                ((xa[4]-xa[1])*(xa[4]-xa[2])*(xa[4]-xa[3])*(xa[4]-xa[0])*(xa[4]-xa[5]))
#
# l5 = lambda x: ya[5]*((x-xa[0])*(x-xa[1])*(x-xa[2])*(x-xa[3])*(x-xa[4]))/\
#                ((xa[5]-xa[1])*(xa[5]-xa[2])*(xa[5]-xa[3])*(xa[5]-xa[0])*(xa[5]-xa[4]))



f1 = CubicSpline(xa, ya, bc_type='natural')
f2 = CubicSpline(xa, ya)
f3 = CubicSpline(xa, ya, bc_type='clamped')



plt.scatter(xa, ya)

plt.plot(x_ew, lagrange_method(xa, ya, x_ew), 'r', label='lagrage method')
plt.plot(x_ew, f1(x_ew), 'b', label='cubic spline(natural)')
plt.plot(x_ew, f2(x_ew), 'g', label='cubic spline(kot-a-nkot)')
plt.plot(x_ew, f3(x_ew), 'purple', label='cubic spline(clamped)')

plt.title('Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()