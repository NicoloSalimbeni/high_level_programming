"""exercise 4 week 0 on string"""

s = "Ciao ciao a"
s = s.lower()

results = {}

for c in s:
    if c in results:
        results[c] += 1
    else:
        results[c] = 1

print(results)
