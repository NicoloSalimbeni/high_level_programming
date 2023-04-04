"""exercise 4 week 3"""

# Use np.linspace to create an array of 100 entries between 0-2π (includsive).
#     Extract every 10th element using slice notation
#     Reverse the array using slice notation
#     Extract elements where the absolute difference between the sine and
#     cosine functions evaluated at that element is less than 0.1
#     Make a plot showing the sin and cos functions and indicate where
#     they are close

import numpy as np
import matplotlib.pyplot as plt

# create the array
a = np.linspace(0, 2 * np.pi, 100)
print("\n", a, "\n")

# extract every 10 element with slice notation
b = a[::10]
print("\n", b, "\n")

# reverse using slice notation
c = a[::-1]
print("\n", c, "\n")

# entries where |sin(xi)-cos(xi)|<0.1
mask = (abs(np.sin(a) - np.cos(a)) < 0.1)
d = a[mask]
print("\n", d, "\n")

# plot
plt.plot(a, np.sin(a), linewidth=2.0, color='g', label='sin')
plt.plot(a, np.cos(a), linewidth=2.0, color='b', label='cos')
plt.scatter(a[mask], np.sin(a[mask]), color='r', label="intersection points")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine functions")

plt.legend()
plt.show()
