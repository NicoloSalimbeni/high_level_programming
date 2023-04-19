"""exercise 3 week 4"""
# Load the saved txt file of point 2 and convert
# it to a csv file (by hand)

import numpy as np

my_matrix = np.loadtxt("matrix.txt")

# now csv conversion by hand
# it consist in sobstitute every " " with ","
np.savetxt("matrix_to_csv.csv", my_matrix, delimiter=',', fmt="%.2f")
