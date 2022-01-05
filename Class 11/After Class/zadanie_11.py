# Zadanie 11

class Student():
    university = "UEK Kraków"
    number = 10000
    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        Student.number += 1
        self.id = Student.number

    def __str__(self):
        return f"{self.id}, {self.name} {self.surname}, {self.field}, {Student.university}"


s1 = Student("Jan", "Kowalski", "Informatyka")
s2 = Student("Adam", "Nowak", "Ekonomia")
s3 = Student("Joanna", "Kot", "Prawo")
print(s1)
print(s2)
print(s3)