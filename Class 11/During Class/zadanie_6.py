#Zadanie 6

class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello everyone! I\'m {self.name}')


class Teacher(Person):
    def __init__(self, name, university):
        self.university = university
        super().__init__(name)

    def say(self):
        print(f'I work as a teacher at {self.university}')

    def bye(self):
        print(f'And now {self.name} is telling you goodbye!')


t = Teacher('Johnny', 'UEK')
t.greet()
t.say()
t.bye()

# a
    # class Teacher(Person):
# b
    # Person - bazowa
    # Teacher - pochodna
# c
    # 1 cecha
    # 1 zachowanie
# d
    # 1 cecha
    # 2 zachowania
# e
    # dziedziczy cechę self.name i zachowanie greet()
# f
    #
# g
    #
# h
    #