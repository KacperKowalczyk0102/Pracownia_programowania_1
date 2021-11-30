# Zadanie 4

def f4(d):
    suma = 0
    for k, v in d.items():
        for n in v:
            if n >= 5 and n <= 10:
                suma = suma + n

    return suma
