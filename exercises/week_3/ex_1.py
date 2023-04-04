"""exercise 1 week 3"""
# 1. Find the row, column and overall means for the following matrix:
import numpy as np

m = np.arange(12).reshape((3, 4))
print("m:\n", m)
print("mean of columns= ", np.mean(m, 0))
print("mean of rows= ", np.mean(m, 1))
print("total mean= ", np.mean(m))
