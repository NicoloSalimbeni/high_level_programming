"""exercise 4 week 1 recursion"""
# wrie factorial with and without recursion technique

# a) with no rectursion


def factorial_1(x):
    """factorial with no recursion"""
    factorial = 1
    if x == 0:
        return 1
    for i in range(1, x):
        factorial *= i
    return factorial * x


print(factorial_1(5))

# b) with recursion


def factorial_2(x):
    """factorial with recursion"""
    if x - 1 < 1:
        return 1
    return x * factorial_2(x - 1)


print(factorial_2(5))
