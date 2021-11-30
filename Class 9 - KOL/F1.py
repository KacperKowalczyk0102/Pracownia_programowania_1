# Zadanie 1

def f1(a):
    lp = 0
    for x in a:
        if x % 2 == 0 and x > 8:
            lp = lp + 1
    return lp