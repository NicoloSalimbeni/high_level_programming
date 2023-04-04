"""exercise 7 week 0"""
# Create a list of the cubes of x for x in [0, 10] using:
# a) a for loop
# b) a list comprehension

# a)
cubes = []
for x in range(0, 11):
    cubes.append(x * x * x)

print(cubes)

# b)
cubes = [x * x * x for x in range(0, 11)]

print(cubes)
