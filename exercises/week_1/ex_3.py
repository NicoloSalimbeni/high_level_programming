"""exercise 3 week 1"""
# 3 Write a decorator hello that makes every wrapped function print “Hello!”,
# i.e. something like:


def square(x):
    """general function"""
    return x * x


def say_hi(func):
    """add print hello before ant operation"""

    def wrapper(x):
        print("Hello")
        return func(x)

    return wrapper


new_function = say_hi(square)
print(new_function(3))
