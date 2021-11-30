# Zadanie 5

def f5(c):
    file = open("poem.txt", "r")
    lp = 0
    for line in file:
        if c in line:
            lp = lp + 1

    return lp
