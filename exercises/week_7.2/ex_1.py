"""exercise 1 week 7.2"""
import matplotlib.pyplot as plt
import numpy as np
import scipy

max_speeds = np.load('./data/max-speeds.npy')
years_nb = max_speeds.shape[0]

cprob = np.arange(1, years_nb + 1) / (years_nb + 1)
sorted_max_speeds = np.sort(max_speeds)

quantile_func = scipy.interpolate.UnivariateSpline(cprob, sorted_max_speeds)
plt.scatter(cprob, sorted_max_speeds)
plt.plot(cprob, quantile_func(cprob))
plt.xlabel("cumulative probability")
plt.ylabel("max wind speed $m/s$")
plt.show()

fifty_prob = 1. - 0.02
fifty_wind = quantile_func(fifty_prob)

print("The 50 years maxima is estimated to be:", fifty_wind, "m/s")
