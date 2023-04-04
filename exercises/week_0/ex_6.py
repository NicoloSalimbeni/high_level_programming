"""ex 6 week 0"""
# Combination of functions
#
# Write two functions - one that returns the square of a number,
# and one that returns the cube. Now write a third function that
# returns the number raised to the 6th power using the two previous functions.


def square(x):
    """square of a number"""
    return x * x


def cube(x):
    """cube  of a number"""
    return x * x * x


def to_the_six(x):
    """risa a number to the 6th"""
    return square(cube(x))


print(to_the_six(2))
