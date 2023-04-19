"""exercise 2 week 4"""
# Create a random matrix of 5x5 and then save it to a file named "data.txt"

import numpy as np

my_matrix = np.random.rand(5, 5)
file_name = "matrix.txt"

with open(file_name, mode='w') as f:
    for line in my_matrix:
        for column in line:
            f.write(str(column))
            f.write(" ")
        f.write("\n")

# or using a numpy built in function
np.savetxt(file_name, my_matrix, fmt="%.2f")
