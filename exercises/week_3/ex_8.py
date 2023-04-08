"""exercise 8 week 3 on random generations"""
# Diffusion using random walk
#
# Consider a simple random walk process: at each step in time, a walker jumps
# right or left (+1 or -1) with equal probability. The goal is to find the
# typical distance from the origin of a random walker after a given amount of
# time. To do that, let's simulate many walkers and create a 2D array with
# each walker as a raw and the actual time evolution as columns
#
#   - Take 1000 walkers and let them walk for 200 steps
#   -Use randint to create a 2D array of size walkers x steps with values
#     -1 or 1
#   -Build the actual walking distances for each walker (i.e. another 2D
#     array "summing on each raw")
#   -Take the square of that 2D array (elementwise)
#   -Compute the mean of the squared distances at each step (i.e. the mean
#     along the columns)
#   -Plot the average distances (sqrt(distance**2)) as a function of time
#     (step)
#
# Did you get what you expected?
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# can't use randint because it includes 0
n_walkers = 200
n_steps = 1000

a = npr.rand(n_walkers, n_steps)
for i in range(0, n_walkers):
    for j in range(0, n_steps):
        if a[i, j] <= 0.5:
            a[i, j] = -1
        elif a[i, j] > 0.5:
            a[i, j] = 1

# print(a)
# 2d array that contains the position after each number of steps
positions = np.array([[np.sum(a[i][:j]) for j in range(n_steps + 1)]
                      for i in range(n_walkers)])
# print("positions:\n", positions)

# mean of the columns after a elementwise square
meansq_positions = np.mean(np.square(positions), axis=0)
# print("mean positions:\n", meansq_positions)

# plot
step = np.arange(0, n_steps + 1)
plt.plot(step, np.sqrt(meansq_positions), 'r-')
plt.xlabel('time')
plt.ylabel('mean square root position')
plt.show()
