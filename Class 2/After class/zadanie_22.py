# Zad 22
print("Zadanie 22")
import random

ran = random.randrange(1, 7)
print("(Zakres 1-6)")
user = int(input("Odgadnij liczbę oczek: "))

if user >= 1 and user <= 6:
    if ran == user:
        print(True)
    else:
        print(False)
else:
    print("Liczba z poza zakresu !!!")

