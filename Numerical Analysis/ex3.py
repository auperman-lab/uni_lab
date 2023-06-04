import numpy as np
import matplotlib.pyplot as plt


def runge_kutta(A, D, t0, tn, dt, U0, R0):

    steps = int((tn - t0) / dt)

    t = np.linspace(t0, tn, steps + 1)

    U = np.zeros(steps + 1)
    R = np.zeros(steps + 1)

    U[0] = U0
    R[0] = R0

    for i in range(steps):
        k1u = dt * (A(t[i]) - D(t[i]))
        k1r = dt * (D(t[i]) - A(t[i]))

        k3u = k2u = dt * (A(t[i] + dt / 2) - D(t[i] + dt / 2))
        k3r = k2r = dt * (D(t[i] + dt / 2) - A(t[i] + dt / 2))

        # k3r = dt * (-A(t[i] + dt / 2) + D(t[i] + dt / 2) - U[i] - k2u / 2)

        k4u = dt * (A(t[i] + dt) - D(t[i] + dt))
        k4r = dt * (D(t[i] + dt) - A(t[i] + dt))

        U[i + 1] = U[i] + (k1u + 2 * k2u + 2 * k3u + k4u) / 6
        R[i + 1] = R[i] + (k1r + 2 * k2r + 2 * k3r + k4r) / 6

    return t, U, R


def arrival_rate(t):
    return 5 * np.sin(t)


def departure_rate(t):
    return 2 * np.exp(t)


in_t = 0
step = 0.001
fin_t = 5
in_U = 0
in_R = 1

t, U, R = runge_kutta(arrival_rate, departure_rate, in_t, fin_t, step, in_U, in_R)

plt.plot(t, R, color='b', label='Total Available Resources')
plt.plot(t, U, color='r', label='Resource Utilisation')
plt.xlabel('time, s')
plt.ylabel('value, units')
plt.legend()
plt.show()
