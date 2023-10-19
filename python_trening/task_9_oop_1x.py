# Создаём новый класс "Input"
class Input:

    # описываем аргумент Loc при инициализации
    def __init__(self, loc, text):
        self.Loc = loc
        self.text = text

    def searchbar(self):
        return 'Кнопка поиска - {}'.format(self.Loc) + ' - "{}"'.format(self.text)


# создаём объект search, относящийся к классу Input
search = Input('input#search', 'Searchbutton')

# выводин в консоль значение аргумента loc объекта search
# print(search.Loc, search.text)
print(search.searchbar())


class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


button = Button('just#button', 'top_on_list')
print(button.text, button.loc)


class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


name = Title('name#words', 'top_on_list')
print(name.text, name.loc)


class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


jump = Link('link#word', 'midside_list')
print(jump.text, jump.loc)
