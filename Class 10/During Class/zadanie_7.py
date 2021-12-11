# Zadanie 7

class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'UEK'

    # object bahaviors (methods)
    def print_name(self):
        print(self.name)

u1 = University()
u1.print_name()
