# Zadanie 29

# 29. Napisz program obliczający sumę i średnią arytmetyczną liczb wprowadzanych z klawiatury.
# Wpisanie 0 kończy wprowadzanie cyfr.

numbers = []
actual = False
while (actual == False):
    nr = int(input("Podaj liczbę: "))
    if (nr == 0):
        actual = True
    else:
        numbers.append(nr)

sum = 0
for item in numbers:
    sum += item

mean = 0
quantity = len(numbers)
mean = sum/quantity

print(f"WYNIK: \nPodanych liczb: {quantity}, \nSuma: {sum}, \nŚrednia: {mean}")


