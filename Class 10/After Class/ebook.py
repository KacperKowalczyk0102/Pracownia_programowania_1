# E-book module

class E_book:

    def __init__(self, title, author, pages):
        self.is_open = False
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1


    def open(self):
        if self.is_open == False:
            self.is_open = True
        else:
            print("Book is already open!")


    def close(self):
        if self.is_open == True:
            self.is_open = False
        else:
            print("Book is already closed!")


    def status(self):
        print("Status:")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")
        print(f"\tNumber of pages: {self.pages}")
        print(f"\tCurrent page: {self.current_page}")


    def read(self, n):
       if self.is_open == True:
            self.current_page = self.current_page + n
       else:
           print("The book is closed!")