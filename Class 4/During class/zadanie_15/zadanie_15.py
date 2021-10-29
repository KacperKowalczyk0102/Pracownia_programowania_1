# Zadanie 15

import mymath


def one_attempt():
    x = mymath.read_number()
    y = mymath.generate_number()
    
    if x == y:
        print("BRAWO! Odgadłeś liczbę!")
    else:
        print(f"Twoja liczba: {x} | Los: {y}")
        print("Nie udało sie ...")
        one_attempt()

one_attempt()

