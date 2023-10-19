from task_9_checks import Checks  # Импорт класса Checks из task_checks.py


class Input(Checks):  # Наследование от класса Checks

    def __init__(self, loc, text):
        super().__init__(loc)  # Вызов инициализатора родительского класса
        self.text = text

    def searchbar(self):
        return 'Кнопка поиска - {}'.format(self.loc) + ' - "{}"'.format(self.text)


# создаём объект search, относящийся к классу Input
search = Input('input#search', 'Searchbutton')

# выводин в консоль значение аргумента loc объекта search
# print(search.Loc, search.text)
print(search.searchbar())


class Button(Checks):  # Наследование от класса Checks
    def __init__(self, text, loc):
        super().__init__(loc)  # Вызов инициализатора родительского класса
        self.text = text


class Title(Checks):  # Наследование от класса Checks
    def __init__(self, text, loc):
        super().__init__(loc)  # Вызов инициализатора родительского класса
        self.text = text


class Link(Checks):  # Наследование от класса Checks
    def __init__(self, text, loc):
        super().__init__(loc)  # Вызов инициализатора родительского класса
        self.text = text


# Создание объектов классов

# search = Input('input#search', 'Searchbutton')
button = Button('just#button', 'top_on_list')
name = Title('name#words', 'top_on_list')
jump = Link('link#word', 'midside_list')

# Вызов метода check_text() для каждого объекта и печать результата в консоль
# print(search.check_text())
print(button.check_text())
print(name.check_text())
print(jump.check_text())
