"""exercise 1 week 4"""
# Create a random list of number and then save it to a text file
# named "simple_data.txt"

import numpy as np

file_name = "simple_file.txt"
l_random = np.random.rand(10)

with open(file_name, mode='w') as f:
    for line in l_random:
        f.write(str(line))
        f.write("\n")
