# Zadanie 28

# 28. Napisz program wyświetlający pierwsze pięćdziesiąt słów ciągu Fibonacciego.
# Sekwencję definiuje się następująco: pierwszy składnik jest równy 0, drugi jest równy 1,
# każdy kolejny składnik jest sumą dwóch poprzednich. Przykładowy wynik poniżej.

a = 0
b = 1
n = 10

for i in range(n):
    print(f"{a}", end=" ")
    b += a
    a + b
    a = b - a



