"""ex 1 week 1"""
# Write the following as a list comprehension
# 1
ans = []
for i in range(3):
    for j in range(4):
        ans.append((i, j))
print(ans)

# as a list comprehension
ans = [(i, j) for i in range(3) for j in range(4)]
print(ans)

# 2
ans = map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(5)))
print(list(ans))

ans = [x**2 for x in range(5) if x % 2 == 0]
print(ans)
