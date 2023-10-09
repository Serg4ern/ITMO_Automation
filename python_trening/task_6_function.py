# определяем функцию
def add(x, y):
    return x + y

# вызываем функцию
print(add(1, 2))

print(add('i a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))
print(arg(2, 2))

# при введении необязательного аргумента, его тип задаётся жёстко
# print(arg(2, 2, '1', 1)) # - такой вызов функции ведёт к ошибке

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))
# print(range_arg('1', '2', d='3', '4')) # - нарушение порядка вызова аргументов

def tpl(a=(1, 2, 3, 4)):
    return a[0]

print(tpl())

def Scrcl(radius, pi=3.14159):
    return pi*(radius**2)

print(Scrcl(9))
