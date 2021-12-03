# F1

def f1(a, c):
    lp = 0
    for i in range(len(a)):
        for j in a[i]:
            if j == c:
                lp = lp + 1
    return lp