def task_1(numb: int, drob: float, mesg: str, nabr: list, flag: bool) -> str:
    nut = str(type(numb))[7:-1]
    drt = str(type(drob))[7:-1]
    mst = str(type(mesg))[7:-1]
    nat = str(type(nabr))[7:-1]
    flt = str(type(flag))[7:-1]
    return   ('numb - относится к типу ' + nut + '\n'
            + 'drob - относится к типу ' + drt + '\n'
            + 'mesg - относится к типу ' + mst + '\n'
            + 'nabr - относится к типу ' + nat + '\n'
            + 'flag - относится к типу ' + flt)


print(task_1(123, 1.23, 'one_two_three', [10, 11, 12], True))


def task_2(a = [1, 2, 3, 5, 8, 13, 21]) -> tuple: # в списке числа Фибоначчи
    first3 = (a[0], a[1], a[2])
    return first3


print(task_2()) # в консоль выводится кортеж


def task_3(dig: float) -> float:
    return dig ** 2


print(task_3(3.14))

