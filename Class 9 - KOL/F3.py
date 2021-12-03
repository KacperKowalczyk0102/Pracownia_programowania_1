# F3

def f3(t):
    t = t.split("=")
    r = t[1]
    n = t[0].split("+")
    
    if ( int(n[0]) + int(n[1]) ) == int(r):
        return True
    else:
        return False
    