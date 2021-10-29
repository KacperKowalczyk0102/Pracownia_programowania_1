# Zadanie 18

def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)

    print(f"Suma cyfr w liczbie to: {suma}")

liczba = "7182"
suma_cyfr(liczba)