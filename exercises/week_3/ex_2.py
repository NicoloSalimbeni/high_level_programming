"""exercisi 2 week 3"""
import numpy as np
# Find the outer product of the following two vecotrs
#
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
#
# Do this in the following ways:
#
#     Using the function outer in numpy
#     Using a nested for loop or list comprehension
#     Using numpy broadcasting operatoins

# using outer function
print("default function:\n", np.outer(u, v), "\n")

# using list comprehension
manual = np.array([[i * j for j in v] for i in u])
print("defualt manual:\n", manual, "\n")

# using numpy broadcasting operations
u = u.reshape(4, 1)
broad = u * v
print("broadcasting operation:\n", broad)
