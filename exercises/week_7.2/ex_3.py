"""exercise 3 week 7.2"""
#  2D minimization of a six-hump camelback function
#
# 𝑓(𝑥,𝑦)=(4−2.1𝑥^2+𝑥^4/3)𝑥^2+𝑥𝑦+(4𝑦^2−4)𝑦^2
#
# has multiple global and local minima. Find the global minima of this function
#
# Hints:
#
#     Variables can be restricted to −2<𝑥<2 and −1<𝑦<1.
#     Use numpy.meshgrid() and pylab.imshow() to find visually the regions.
#     Use scipy.optimize.minimize(), optionally trying out several of its
#     methods.
#
# How many global minima are there, and what is the function value at those
# points? What happens for an initial guess of (𝑥,𝑦)=(0,0)?

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def func(x):
    """function to minimize"""
    z = x[0]**2 * (4 - 2.1 * x[0]**2 +
                   x[0]**4 / 3) + x[0] * x[1] + x[1]**2 * (4 * x[1]**2 - 4)
    return z


x_tmp = np.linspace(-2, 2, 100)
y_tmp = np.linspace(-1, 1, 100)
xx, yy = np.meshgrid(x_tmp, y_tmp)

z = func([xx, yy])

# plot, i prefer contour over imshow
fig, ax = plt.subplots(1, 1)
cp = ax.contourf(xx, yy, z)
fig.colorbar(cp)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("f(x,y)")

plt.show()

# look for minimums:
initial_guess = np.array([0, -0.5])
result_down = sp.optimize.minimize(func, initial_guess)

initial_guess = np.array([0, 0.5])
result_up = sp.optimize.minimize(func, initial_guess)
print("we have two minimums:")
print("upper: ", result_up["x"])
print("lower: ", result_down["x"])
