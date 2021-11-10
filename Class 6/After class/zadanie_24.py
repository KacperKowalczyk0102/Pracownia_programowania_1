# Zadanie 24

numbers = [4,36,12,28,9,44,5]

def bigger(a):
    lp = 0
    for n in numbers:
        if n > a:
            lp += 1

    return lp


a =  int(input("Podaj liczbę: "))
print(f"Liczb większych niż {a} jest {bigger(a)}")

