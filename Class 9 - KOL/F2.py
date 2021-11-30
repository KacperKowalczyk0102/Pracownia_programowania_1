# Zadanie 2

def f2(a1, a2):
    d1 = 0
    d2 = 0
    for x in a1:
        if len(str(x)) == 2:
            d1 = d1 + 1

    for y in a2:
        if len(str(y)) == 2:
            d2 = d2 + 1

    if d1 == d2:
        return True
    else:
        return False

