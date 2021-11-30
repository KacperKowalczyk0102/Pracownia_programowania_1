# Zadanie 6

def f6(g,n1,n2):
    file = open("people.csv", "r")
    lp = 0
    for line in file:
        line = line[:-1]
        line = line.split(",")
        if line[3] == g and (n1 <= int(line[2]) <= n2):
            lp = lp + 1

    return lp
