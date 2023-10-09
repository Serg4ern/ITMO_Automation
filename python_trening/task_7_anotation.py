a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))


def lenstrng(s: str = '') -> int:
    return len(s)


print(lenstrng('python'))


def maxlst(n: list, m: list) -> int:
    return max(len(n), len(m))


print(maxlst([0, 8], [1, 2, 3]))


def lstappnd(inputl: list, addx):
    inputl.append(addx)
    return inputl


print(lstappnd(['cat', ' ', 69, ' '], ('dog', 's', ' ', 78)))


def summlist(inp: list):
    while len(inp) > 1:
        inp[0] = inp[0] + inp[1]
        inp.pop(1)
    return inp[0]

my_list = [1, 2, 3, 5, 8]
print(summlist(my_list))

