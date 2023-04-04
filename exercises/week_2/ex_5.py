"""exercise 5 week 2 on precision"""
# Write a function that takes in input three parameters 𝑎, 𝑏 and 𝑐 and prints
# out the two solutions to the quadratic equation 𝑎𝑥2+𝑏𝑥+𝑐=0 using the
# standard formula (a) use the program to compute the solution for a=0.001,
# b=1000 and c=0.001

# (b) re-express the standard solution formula by multiplying top and bottom by
# -b+-sqrt{b^2-4ac} and again find the solution for a=0.001, b=1000 and c=0.001
# How does it compare with what previously obtained? Why?

# (c) write a function that compute the roots of a quadratic equation
# accurately in all cases

from math import sqrt
from numpy import sign


def Solve1(a, b, c):
    """usual function"""
    sol = [(-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
           (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)]
    return sol


def Solve2(a, b, c):
    """usual function"""
    d = b**2 - 4 * a * c
    sol_plus = (d - b**2) / (2 * a * (b + sqrt(d)))
    sol_minus = (d - b**2) / (2 * a * (b - sqrt(d)))

    sol = [sol_plus, sol_minus]
    return sol


def SolveStable(a, b, c):
    """stable function"""
    sol_plus = -2 * c / (b + sign(b) * sqrt(b**2 - 4 * a * c))
    sol_minus = c / (a * sol_plus)
    return [sol_plus, sol_minus]


a1 = 0.001
b1 = 1000
c1 = 0.001
print("usual formula: ", Solve1(a1, b1, c1))
print("rationalized formula: ", Solve2(a1, b1, c1))
print("stable function: ", SolveStable(a1, b1, c1))
