# F6

def f6(x, n):
    a1 = 1
    r = x    
    an = a1
    
    lp = 1
    while lp < n:
        temp = an
        an = temp + r
        if an % 2 != 0:
            lp += 1
            
    return an
        

# a(n+1) = an + r

# r = 2
# n = 8
# 1, 3, 5, 7, 9, 11, 13, 15

# r = 3
# n = 4
# 1, 4, 7, 10, 13, 16, 19


    
    
        