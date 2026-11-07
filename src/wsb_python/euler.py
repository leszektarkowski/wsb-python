"""If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

n = []
for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        n.append(i)

#print(n)
print(f"Sum = {sum(n)}")

"""
2 ** 15 = 32768
3 + 2 + 7 + 6 + 8 = 26

2 ** 1000 = ....
sum of all digits?
"""

s = 0
n = 0
for i in str(2**1000):
    s += int(i)
    n += 1

print(f"2**1000 has length {n}")
print(f"sum = {s}")

n_list = []
for i in str(2**1000):
    n_list.append(int(i))

print(f"2**1000 has length {len(n_list)}")
print(f"Sum = {sum(n_list)}")

# list comprehension

l = list(range(10))

res = []
for i in l:
    if i > 2:
        res.append(i**3)
print(res)

print([i ** 3 for i in l if i > 2])

print(sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))