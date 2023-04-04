"""exercise 6 week 3"""
# Use broadcasting to create a grid of distances

# Route 66 crosses the following cities in the US: Chicago, Springfield,
# Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque,
# Flagstaff, Los Angeles The corresponding positions in miles
# are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448

#     Construct a 2D grid of distances among each city along Route 66
#     Convert that in km (those savages...)

import numpy as np

d = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
d_T = d.reshape(len(d), 1)
grid = np.abs(d_T - d)
print("grid in miles:\n", grid)
print("grid in km:\n", 1.60934 * grid)
