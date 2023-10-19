class Page:

    def __init__(self, url):
        self.link = url

    def get(self):
#        return '{}'.format(self.link)
        print(self.link)

home = Page('https://google.com')
#print(home.get())
home.get()

