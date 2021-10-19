# Zadanie 21

# 21. Napisz program, który utworzy tabliczkę mnożenia z zakresu od 1 do 10
# dla dowolnej liczby wprowadzonej przez użytkownika.

number = int(input("Podaj liczbę: "))

for x in range(1, 11):
    result = number * x
    print(f"{result} X {x} = {result}")