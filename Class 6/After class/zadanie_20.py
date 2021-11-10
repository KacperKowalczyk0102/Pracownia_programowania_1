# Zadanie 20

array = [15, 38, 7, 23, 14]

def occurs(number, array):
    for n in array:
        if n == number:
            return "Występuje"
    else:
        return "Nie występuje"

number = int(input("Podaj liczbę: "))
print(f"Liczba: {number}")
print(f"Tablica: {array}")
print(occurs(number, array))


