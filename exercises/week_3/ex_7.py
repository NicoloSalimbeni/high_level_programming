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
import numpy as np
import matplotlib.pyplot as plt


# find prime numbers with ordinary sieve algorithm
def Prime_Numbers(N):
    """return a list of prime numbers up to N"""
    v = np.arange(0, N)
    primes = [True] * N
    for i in range(0, int(np.sqrt(N))):
        if i in (0, 1):
            primes[i] = True
        else:
            if primes[i]:
                count = 0
                while i * i + count * i < N:
                    primes[i * i + count * i] = False
                    count += 1

    return v[primes]


print(Prime_Numbers(1000))

times = []
for i in range(100, 21000, 1000):
    time_in = time.time()
    Prime_Numbers(i)
    times.append(time.time() - time_in)

plt.plot(range(100, 21000, 1000), times)
plt.xlabel("N")
plt.ylabel("time")
plt.show()
