a = 2
print(a, "относится к типу ", type(a))

b = 15.0001
print(b, "относится к типу ", type(b))

c = 1+2j
print(c, "Комплексное число? ", isinstance(c, complex))

print(6 + 2)
print(6 - 2)
print(6 * 2)
print(6 / 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(6 ** 2)

x = 'types' + ":" + ' ' + str(type(a)) + ', ' + str(type(b))
print(x)
