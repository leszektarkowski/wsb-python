l = [1, 2, 3, 4]
d = {"a": 1, "b":2, "c":3}

for i in l:
    print(i)

print(20*"-")

for k in d:
    print(k)

for k in d:
    v = d[k]
    print(f"key {k}, value {v}")

print(20*"-")

# items([('a', 1), ('b', 2), ('c', 3)])
for k, v in d.items():
    print(f"key {k}, value {v}")

print(20*"-")

# items([('a', 1), ('b', 2), ('c', 3)])
for item in d.items():
    print(f"key {item[0]}, value {item[1]}")
