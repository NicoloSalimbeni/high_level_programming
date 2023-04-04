"""exercise 3 week 2 on under/overflow"""
# Write a program to determine the underflow and overflow limits
# (within a factor of 2) for python on your computer.
# Tips: define two variables inizialized to 1 and halve/double
# them enough time to exceed the under/over-flow limits

number = 1

while number / 2 > 0:
    number /= 2
    if number / 2 == 0:
        print("underflow occur at: ", number)

number = 1.

while number * 2 < float("inf"):
    number *= 2
    if number * 2 == float("inf"):
        print("overflow occur at: ", number)
