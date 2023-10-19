# class Rectangle:
#
#     def __init__(self, w: float, h: float):
#         self.wide = w
#         self.high = h
#
#     def area(self):
#         a = self.wide * self.high
#         return "Площадь прамоугольника - " + str(a)
#
#     def perim(self):
#         p = 2 * (self.wide + self.high)
#         return "Периметр прямоугольника - " + str(p)
#
#
# x1 = Rectangle(3, 4)
# x2 = Rectangle(0.5, 100)
# x3 = Rectangle(44, 9)
# print("Для x1:", '\n', x1.area(), '\n', x1.perim(), '\n')
# print("Для x2:", '\n', x2.area(), '\n', x2.perim(), '\n')
# print("Для x3:", '\n', x3.area(), '\n', x3.perim(), '\n')
#
#
# class Math:
#
#     def __init__(self, numb_a: float, numb_b: float):
#         self.a = numb_a
#         self.b = numb_b
#
#     def addiction(self):
#         print('сумма - ', self.a + self.b)
#
#     def multipilication(self):
#         print('произведение - ', self.a * self.b)
#
#     def division(self):
#         print('деление - ', self.a / self.b)
#
#     def subtraction(self):
#         print('разность - ', self.a - self.b)
#
#
# x = float(input('введите первое число: '))
# y = float(input('введите второе число: '))
# twonumb = Math(x, y)
# twonumb.addiction()
# twonumb.multipilication()
# twonumb.division()
# twonumb.subtraction()


class SubMenu:

    type: str = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.loc = loc

    def push_btn(self):
        print(f'Клик по кнопке {self.text}')


text_box = SubMenu('Text Box')
check_box = SubMenu('Check Box')
radio = SubMenu('Radio Button')
web_tables = SubMenu('Web Tables')
buttons = SubMenu('Buttons')
links = SubMenu('Links')
broken_links = SubMenu('Broken Links - Images')
upload_dwnl = SubMenu('Upload and Download')
dynamic = SubMenu('Dynamic Properties')

text_box.push_btn()
check_box.push_btn()
radio.push_btn()
web_tables.push_btn()
buttons.push_btn()
links.push_btn()
broken_links.push_btn()
upload_dwnl.push_btn()
dynamic.push_btn()

