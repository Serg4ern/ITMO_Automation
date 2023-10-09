# def two_max(a, b):
#     if a > b:
#         return str(a) + ' > ' + str(b)
#     elif b > a:
#         return str(b) + ' > ' + str(a)
#     else:
#         return 'Числа равны'
#
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(two_max(a, b))
#
#
# def two_135(a, b):
#     if abs(a-b) == 135:
#         print('Yes')
#     else:
#         print('No')
#
# print('Числа отличаются на 135?')
# two_135(a, b)
#


# def seasoNumb(m: int):
#     if 2 < m < 6:
#         print('spring')
#     elif 5 < m < 9:
#         print('summer')
#     elif 8 < m < 12:
#         print('autumn')
#     elif 0 < m < 3 or m == 12:
#         print('winter')
#     else:
#         print('Wrong number!')
#
#
# m = int(input('Month number: '))
# seasoNumb(m)


# def threenumb(x, y, z):
#     if x > 10 and y > 10 and z > 10:
#         print('yes')
#     else:
#         print('no')
#
#
# x = float(input('x = '))
# y = float(input('y = '))
# z = float(input('z = '))
# threenumb(x, y, z)


# def max5(s):
#     ls = s.split()
#     l = []
#     for i in ls:
#         x = float(i)
#         if x > 0:
#             l.append(x)
#     print('Количество положительных чисел: ', len(l))
#
# s = input('введите пять чисел через пробел: ')
# max5(s)


def year_month_sum(g: int, p: int):
    return g*365 + p*29

g = 15
p = 3
print(year_month_sum(g, p))

