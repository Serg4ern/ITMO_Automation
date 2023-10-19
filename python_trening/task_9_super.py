class A:

    def __init__(self, numb):
        self.nu = numb


class B(A):

    def __init__(self, numb):
        super().__init__(numb)
        self.y = self.nu + 5


x = int(input('input number x: '))

print(B(x).y)

b = B(x)
print(b.y)
