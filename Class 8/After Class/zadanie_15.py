# Zadanie 15
import json

uczniowie = []
def data_input():
    imie = input("Imie: ")
    kierunek = input("Kierunek: ")
    rok = input("Rok: ")
    uczelnia = input("Uczelnia: ")
    uczniowie.append({"imie": imie, "kierunek": kierunek, "rok": rok, "uczelnia": uczelnia})
    next = input('Dodać kolejnego ucznia?')
    if next == "":
        data_input()
    else:
        file = open("student.json", "w")
        json.dump(uczniowie, file, indent=4)
        print("Zapisano dane do pliku")
data_input()


