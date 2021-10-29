# F3

def max4(n1, n2, n3, n4):
    liczby = (n1, n2, n3, n4)
    w = 0
    for i in range(0, len(liczby)):
        if liczby[i] > w:
            w = liczby[i]

    print(w)
