"""exercise 2 week 7.2"""

# The temperature extremes in Alaska for each month,
# starting in January, are given by (in degrees Celcius):
#
# max: 17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18
#
# min: -62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58
#
#     -Plot these temperature extremes.
#     -Define a function that can describe min and max temperatures.
#     -Fit this function to the data with scipy.optimize.curve_fit().
#     -Plot the result. Is the fit reasonable? If not, why?
#     -Is the time offset for min and max temperatures the same within
#     -the fit accuracy?

import numpy as np
import matplotlib.pyplot as plt
import scipy

max_tmp = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18],
                   dtype=np.float64)
min_tmp = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58],
                   dtype=np.float64)
month = np.arange(1, 13, 1)

# plot
plt.scatter(month, max_tmp, label="max")
plt.scatter(month, min_tmp, label="min")
plt.xlabel("month")
plt.ylabel("temperature [°C]")
plt.legend()
plt.title("min max temperature in Alaska")


# fit with gaussians
def gauss(x, N, offset, mu, sigma):
    """gaussiang + offset"""
    return offset + (N / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 /
                                                                (2 * sigma**2))


params_max, cov_max = scipy.optimize.curve_fit(gauss,
                                               month,
                                               max_tmp,
                                               p0=[100, 20, 7.14, 2])
params_min, cov_min = scipy.optimize.curve_fit(gauss, month, min_tmp)

plt.plot(
    month,
    gauss(month, params_max[0], params_max[1], params_max[2], params_max[3]))
plt.plot(
    month,
    gauss(month, params_min[0], params_min[1], params_min[2], params_min[3]))

plt.show()

# here to study the fit we need the chi^2 this package do not have it, you
# should use what they say here:
# https://stackoverflow.com/questions/52591979/how-to-obtain-the-chi-squared-value-as-an-output-of-scipy-optimize-curve-fit
# otherwise you have to perform calculations by hand

gass_max_tmp = [
    gauss(m, params_max[0], params_max[1], params_max[2], params_max[3])
    for m in month
]
gass_min_tmp = [
    gauss(m, params_min[0], params_min[1], params_min[2], params_min[3])
    for m in month
]

gauss_max = np.array(gass_max_tmp)
gauss_min = np.array(gass_min_tmp)

chisq, p = scipy.stats.chisquare(max_tmp, gauss_max, ddof=4)
print("max -> chi^2 =", chisq, " p-value:", p)

chisq_min, p_min = scipy.stats.chisquare(min_tmp, gauss_min, ddof=4)
print("min -> chi^2 =", chisq_min, " p-value:", p_min)
