"""exercise 2 week 6"""
# Produce a scatter plot out of a dataset with two categories
#   -Write a function that generate a 2D datasets of 2 categories.
#    Each category should distribute as a 2D gaussian with a given
#    mean and std (clearly it is better to have different values means..)
#   -Display the dataset in a scatter plot marking the two categories with
#    different marker colors.

import numpy as np
import matplotlib.pyplot as plt


def DateGenerator(mean1, mean2, sigma1, sigma2, n_values):
    """generats the 2D sample"""
    mean = [mean1, mean2]
    cov = [[sigma1, 0], [0, sigma2]]
    dataset = np.random.multivariate_normal(mean, cov, n_values)
    return dataset.T


sample1 = DateGenerator(3, 10, 1, 2, 1000)
sample2 = DateGenerator(10, 3, 1, 2, 1000)
plt.scatter(sample1[0], sample1[1], marker='o', color="red")
plt.scatter(sample2[0], sample2[1], marker='o', color="blue")

plt.xlabel("category 1")
plt.ylabel("category 2")

plt.show()
