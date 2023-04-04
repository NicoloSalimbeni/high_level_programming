"""exercisi 3 week 3"""
# Create a 10 by 6 matrix of random uniform numbers. Set all rows with any
# entry less than 0.1 to be zero
# Hint: Use the following numpy functions - np.random.random, np.any as
# well as Boolean indexing and the axis argument.

import numpy as np

# create the matrix
m = np.random.rand(10, 6)
print("m:\n", m, "\n")

# if a row has an entry less then 0.1 the raw is set to  zero
c = np.any(m < 0.1, 1)

for i in range(m.shape[0]):
    if c[i]:
        m[i] = np.zeros(m.shape[1])

print("m:\n", m, "\n")
