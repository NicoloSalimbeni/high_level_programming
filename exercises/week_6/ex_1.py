"""exercise 1 week 6 on histograms"""
# 1. Kernel Density Estimate
#
# Produce a KDE for a given distribution (by hand, not using seaborn!):
#
#     Fill a numpy array, x, of len(N) (with N=O(100)) with a variable normally
#     distributed, with a given mean a standard deviation
#     Fill an histogram in pyplot taking properly care about the aesthetic
#       use a meaningful number of bins
#       set a proper y axis label
#       set proper value of y axis major ticks labels (e.g. you want to display
#       only integer labels)
#       display the histograms as data points with errors (the error being the
#       poisson uncertainty)
#     for every element of x, create a gaussian with the mean corresponding the
#     element value and std as a parameter that can be tuned. The std default
#     value should be: 1.06∗𝑥.𝑠𝑡𝑑()∗𝑥.𝑠𝑖𝑧𝑒−15.
#
# you can use the scipy function stats.norm() for that.
# In a separate plot (to be placed beside the original histogram), plot all the
# gaussian functions so obtained
# Sum (with np.sum()) all the gaussian functions and normalize the result such
# that the integral matches the integral of the original histogram. For that
# you could use the scipy.integrate.trapz() method

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import norm
import scipy

mu = 3
sigma = 1
x = np.random.normal(loc=10, scale=2, size=800)
fig, ax = plt.subplots(1, 1)
n, bins, _ = ax.hist(x, bins=16, alpha=0.5)
# n = bin high
# bins = all bin edge, lower and upper included

# set labels
ax.set_xlabel("x")
ax.set_ylabel("counts")

# set limits
plt.xlim([2, 18])
plt.ylim([0, 150])

# set ticks
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(15))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

# add error bars
mid = 0.5 * (bins[1:] + bins[:-1])
plt.errorbar(mid, n, yerr=np.sqrt(n), fmt='none')
plt.show()

# ===========  second part fo the exercise with the gaussians ===========
t = np.linspace(-20, 40, 100)
std_err = 1.06 * x.std() * np.power(len(x), 1 / 5)
gaus = []
for mean in x:
    gaus.append(norm.pdf(t, loc=mean, scale=std_err))

for g in gaus:
    plt.plot(t, g)

plt.xlim(-20, 40)

# labels
plt.xlabel("x")
plt.ylabel("gaus(x,std)")

plt.show()

# ========== normalized gaussian
tot_gaus = [0] * len(gaus[0])
for g in gaus:
    tot_gaus = tot_gaus + g

# should be 800, all gaussians are normalized!
integral = scipy.integrate.trapz(tot_gaus, dx=(t.max() - t.min()) / 100)

# histogram integral
bin_width = bins[1] - bins[0]
hist_integral = bin_width * sum(n)
tot_gaus = tot_gaus * hist_integral / integral

plt.plot(t, tot_gaus)
plt.xlabel("x")
plt.ylabel("sum all gaussians normalized to initial histogram")

plt.show()
