a = (1, 2)
b = a + ("a", "b")
c = (1, 2, "a", 0b101, 9.5e6)

print(a)
print(b)
print(c[0], c[2], c[2:4], c[-1])

print(len(c))
print(c[::-1])  # разворачивается задом наперед

d = (1)
e = (1,)

print(d)
print(e)
