# Zadanie 8

class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'UEK'

    # object bahaviors (methods)
    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


u1 = University()
u1.set_name("AGH")
u1.print_name()