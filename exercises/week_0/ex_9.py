"""exercise 9 week 0"""
# 9. Normalization
# Write a function that takes a tuple of numbers and returns it with the
# entries normalized to one
import math


def normalize(t):
    """normalize a tuple"""
    l_temp = list(t)
    length = 0
    for x in l_temp:
        length += x**2
    length = math.sqrt(length)
    for x in range(0, len(l_temp)):
        l_temp[x] = l_temp[x] / length
    return tuple(l_temp)


a = (1, 1, 1)
print(normalize(a))
