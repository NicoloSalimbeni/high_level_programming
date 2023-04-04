"""exercise 5 week 3"""

# Create a matrix that shows the 10 by 10 multiplication table.
#
#     Find the trace of the matrix
#     Extract the anto-diagonal (this should be
#     array([10, 18, 24, 28, 30, 30, 28, 24, 18, 10]))
#     Extract the diagnoal offset by 1 upwards
#     (this should be array([ 2,  6, 12, 20, 30, 42, 56, 72, 90]))

import numpy as np

# multiplication matrix
b = np.array(range(1, 11, 1))
h = b.reshape(len(b), 1)
a = h * b
print("matrix multiplication:\n", a)

# find the trace
trace = 0
for i in range(0, 10, 1):
    trace += a[i, i]
print("trace: ", trace)

# antidiagonal
a_diag = a[range(9, -1, -1), range(0, 10, 1)]
print("anti-diagonal: ", a_diag)

# diagonal with offset
diag_off = a[range(0, 9, 1), range(1, 10, 1)]
print("diagonal with +1 offset: ", diag_off)
