def fixed_point_iteration(c, x0, tolerance=1e-8):
    x = x0
    for i in range(1000):
        x_new = 2*x - c*x**2
        if abs(x_new - x) < tolerance:
            return print(x_new)
        x = x_new
    print("Failed to converge after 1000 iterations")


c = 1/4
x0 = 0.4

fixed_point_iteration(c, x0)
