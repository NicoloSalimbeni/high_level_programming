"""exercise 8 week 0"""
# 8. Nested list comprehension
# A Pythagorean triple is an integer solution to the Pythagorean theorem
# 𝑎2+𝑏2=𝑐2. The first Pythagorean triple is (3,4,5). Find and put in a tuple
# all unique Pythagorean triples for the positive integers a, b and c less
# than 100.

triples = []

for a in range(1, 101):
    for b in range(a, 101):
        for c in range(b, 101):
            if a**2 + b**2 == c**2:
                triples.append((a, b, c))

print(triples)
