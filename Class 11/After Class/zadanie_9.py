# Zadanie 9

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author =  author
        self.year = year


class Paper_book(Book):
    def __init__(self, pages, title, author, year):
        self.pages = pages
        super().__init__(title, author, year)

    def __str__(self):
        return f"Pages:\t\t {self.pages} \nTitle:\t\t {self.title} \nAuthor:\t\t  {self.author} \nYear:\t\t {self.year} \n"


class Ebook(Book):
    def __init__(self, filename, title, author, year):
        self.filename = filename
        super().__init__(title, author, year)

    def __str__(self):
        return f"File name:\t {self.filename} \nTitle:\t\t {self.title} \nAuthor:\t\t {self.author} \nYear:\t\t {self.year} \n"


p = Paper_book("123", "Pan Tadeusz", "Adam MIckiewicz", "2005")
e = Ebook("pantadeusz.pdf", "Pan Tadeusz", "Adam MIckiewicz", "2005")

print(p)
print(e)