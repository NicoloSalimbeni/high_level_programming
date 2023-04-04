"""exercise 7 week 2 on precision"""
# 7. Consider the integral of the semicircle of radius 1:
# 𝐼=∫1−1(⎯√1−𝑥2)d𝑥
# which it's known to be 𝐼=𝜋2=1.57079632679.... Alternatively we can
# use the Riemann definition of the integral:
# 𝐼=lim𝑁→∞∑𝑘=1𝑁ℎ𝑦𝑘
# with ℎ=2/𝑁 the width of each of the 𝑁 slices the domain is divided
# into and where 𝑦𝑘 is the value of the function at the 𝑘−th slice.

# (a) Write a programe to compute the integral with 𝑁 =100. How does
# the result compares to the true value?

# (b) How much can 𝑁 be increased if the computation needs to be run
# in less than a second? What is the gain in running it for 1 minute?

from math import sqrt
from math import pi
import time
from tqdm import tqdm


def integral(f, N, x_min, x_max):
    """integrate a function"""
    h = (x_max - x_min) / N
    integral_value = 0
    for i in tqdm(range(0, int(N)), leave=False):
        x_i = x_min + h * (i + 0.5)
        integral_value += h * f(x_i)
    return integral_value


def semicircle(x):
    """function of positive semicircle"""
    return sqrt(1 - x * x)


int_n_2 = integral(semicircle, 100, -1, 1)
print("power of 10 \t manual \t\t analytical \t\t (analy-manual)/analy %")
print(2, "\t\t", int_n_2, "\t", pi / 2, "\t",
      (int_n_2 - pi / 2) * 100 / (pi / 2))

n = 8.4
t_init = time.time()
int_n_n = integral(semicircle, pow(10, n), -1, 1)
t_end = time.time()

print(n, "\t\t", int_n_n, "\t", pi / 2, "\t", int_n_n - pi / 2)
print("execution time: ", t_end - t_init)
