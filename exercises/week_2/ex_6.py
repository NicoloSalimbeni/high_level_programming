"""exercise 6 week 2"""
# Write a program that implements the function 𝑓(𝑥)=𝑥(𝑥−1):

# (a) Calculate the derivative of the function at the point 𝑥=1 using the
# derivative definition with 𝛿=10−2.
# d𝑓/d𝑥 = lim 𝛿→0 (𝑓(𝑥+𝛿)−𝑓(𝑥))/𝛿
# Calculate the true value of the same derivative analytically and compare
# with the answer your program gives. The two will not agree perfectly.
# Why not?

# (b) Repeat the calculation for 𝛿=10^−4,10^−6,10^−8,10^−10,10^−12 and 10^−14.
# How does the accuracy scales with 𝛿?


def diff(func, x, d):
    """1st derivative of func in x with increment d"""
    return (func(x + d) - func(x)) / d


def f(x):
    """example function"""
    return x * (x - 1)


def f_1(x):
    """analytical derivative"""
    return 2 * x - 1


print("delta \t\t manual \t\t analytical \t manual-analytical")
for i in range(2, 16, 2):
    print("10^(", i, ")\t", diff(f, 1, pow(10, -1 * i)), "\t", f_1(1), "\t\t",
          diff(f, 1, pow(10, -1 * i)) - f_1(1))
