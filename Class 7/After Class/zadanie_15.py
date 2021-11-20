# Zadanie 15

name = input("Podaj nazwę pliku: ")
name = "files\\" + name + ".txt"
file = open(name, "r")
length = 0
for i in file:
    length += 1
print(f"Liczba wierszy: {length}")