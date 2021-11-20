# Zadanie 19

def czy_w_zakresie(liczba, x, y):
    return bool(liczba >= x and liczba <= y)

if czy_w_zakresie(1, 4, 2):
    print("TAK")
else:
    print("NIE")