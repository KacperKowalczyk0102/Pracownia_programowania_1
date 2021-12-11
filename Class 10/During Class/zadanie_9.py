# Zadanie 9

class University():

    def __init__(self, name, full_name):
        self.name = name
        self.fullname = full_name

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def print_fullname(self):
        print(self.fullname)

    def set_fullname(self, fullname):
        self.fullname = fullname

u1 = University('UEK', "Uniwersytet Ekonomiczny w Krakowie")
# a
u1.print_name()
# b
u1.print_fullname()
# c
u1.set_name("AGH")
# d
u1.set_fullname("Akademia Górniczo-Hutnicza")
# e
u1.print_name()
# f
u1.print_fullname()