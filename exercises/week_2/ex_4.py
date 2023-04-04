"""exercise 4 week 2 on machine precision"""
# Write a program to determine the machine precision

# Tips: define a new variable by adding a smaller and smaller value
# (proceeding similarly to prob. 3) to an original variable and check
# the point where the two are the same

number = 1.5
a = 1
while number != number + a:
    a /= 2

print("precision: ", a)
