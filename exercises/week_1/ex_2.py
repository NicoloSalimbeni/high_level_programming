"""ex 2 week 1"""
# Convert the following function into a pure function with no global variables or side effects
x = 5


def f(a_list):
    """return a list with appended integers from 0 to x-1"""
    for i in range(x):
        a_list.append(i)
    return a_list


alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)  # alist has been changed!


def f1(a_list, n):
    """retrun a list with appended integers from 0 to x-1, no side effects,
    no external viariables"""
    temp = list(a_list)
    for i in range(n):
        temp.append(i)
    return temp


alist = [1, 2, 3]
ans = f1(alist, 5)
print(ans)
print(alist)
