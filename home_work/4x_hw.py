class Car:

    def __init__(self, color, type_car, year):
        self.color = color
        self.type = type_car
        self.year = year

    def start_engn(self):
        print("Автомобиль заведён")

    def stop_engn(self):
        print("Автомобиль заглушен")

    def car_year(self):
        y = int(input('Введите год выпуска: '))
        self.year = y

    def car_type(self):
        t = input('Введите тип авто: ')
        self.type = t

    def car_color(self):
        c = input('Введите цвет авто: ')
        self.color = c


car = Car('белый', 'фаэтон', '1967')
print(f'Старое авто: {car.color} {car.type} {car.year} г.в.')
car.start_engn()
car.stop_engn()
car.car_year()
car.car_type()
car.car_color()
print(f'Новое авто: {car.color} {car.type} {car.year} г.в.')
