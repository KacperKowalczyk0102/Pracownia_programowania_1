# F2

def f2(a1, a2):
    stars = ""
    for i in range(len(a1)):
        if a1[i] in a2:
            stars = stars +"*"
            
    return stars