# F4

def f4(d, n):
    lp = 0
    for x in d:
        if x["age"] > n:
            lp = lp + 1
    
    return lp
