"""exercise 5 week 1 on HOF"""
from math import pi

# 5. Use HOFs (zip in particular) to compute the weight of a circle, a disk and
# a sphere, assuming different radii and different densities:
#
densities = {"Al": [0.5, 1, 2], "Fe": [3, 4, 5], "Pb": [15, 20, 30]}
radii = [1, 2, 3]
#
# where the entries of the dictionary's values are the linear, superficial and
# volumetric densities of the materials respectively.
#
# In particular define a list of three lambda functions using a comprehension
# that computes the circumference, the area and the volume for a given radius.

dimentions = [
    lambda x: 2 * pi * x, lambda x: x**2 * pi, lambda x: 4 * pi * x**3 / 3
]

for element, element_density in densities.items():
    print(element)
    print("weight of circle, disk, sphere: ")
    for r in radii:
        print("radius of: ", r, end=' ')
        values = []
        for dimention, density in zip(dimentions, densities[element]):
            values.append(density * dimention(r))
        print(values)
