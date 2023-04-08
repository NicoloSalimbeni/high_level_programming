"""exercise 7 week 3"""
# Prime numbers sieve: compute the prime numbers in the 0-N (start with N=99)
# range with a sieve (mask).

#     -Constract a shape (100,) boolean array, the mask
#     -Identify the multiples of each number starting from 2 and set
#      accordingly the corresponding mask element
#     -Apply the mask to obtain an array of ordered prime numbers
#     -Check the performances (timeit); how does it scale with N?
#     -Implement the optimization suggested in the sieve of Eratosthenes

# I didn't understood what I have to do

import time
import math
import numpy as np
import matplotlib.pyplot as plt


# find prime numbers with ordinary sieve algorithm
def Prime_Numbers(N):
    """return a list of prime numbers up to N"""
    v = np.arange(2, N)
    primes = [True] * (N - 2)
    for i in range(2, int(np.sqrt(N))):
        if primes[i - 2]:
            count = 0
            while i * i + count * i < N:
                primes[i * i + count * i - 2] = False
                count += 1

    return v[primes]


print(Prime_Numbers(100))

times = []
for i in range(100, 21000, 1000):
    time_in = time.time()
    Prime_Numbers(i)
    times.append(time.time() - time_in)

plt.plot(range(100, 21000, 1000), times)
plt.xlabel("N")
plt.ylabel("time")
plt.show()

# with better method


def Prime_Numbers_Euler(N):
    """return prime numbers up to N, better algorithm"""
    a = np.arange(2, N)
    for n in a:
        if n > 0:
            for j in range(2, math.ceil(N / n)):
                a[j * n - 2] = 0
    mask = a > 0
    primes = a[mask]
    np.insert(primes, 1, 1)
    return primes


print(Prime_Numbers_Euler(100))

times = []
for i in range(100, 21000, 1000):
    time_in = time.time()
    Prime_Numbers_Euler(i)
    times.append(time.time() - time_in)

plt.plot(range(100, 21000, 1000), times)
plt.xlabel("N")
plt.ylabel("time")
plt.show()
