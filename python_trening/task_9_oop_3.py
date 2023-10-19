class Soda:

    # ** def __init__(self, dob):
    def __init__(self, dob=None):
        self.dobavka = dob

    def show_my_drink(self):
        if self.dobavka:
            # print('Газировка и {}'.format(self.dobavka))
            print(f'Газировка и {self.dobavka}')
        else:
            print('Обычная газировка')


# ** tonik = Soda('')
tonik = Soda()
cola = Soda('E211')
tonik.show_my_drink()
cola.show_my_drink()
