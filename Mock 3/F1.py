class C:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name[0] + self.surname[0]

