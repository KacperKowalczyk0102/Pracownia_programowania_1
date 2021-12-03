# F5

def f5(c, n):
    file = open("beautybeast.txt", "r")
    m = 0
    row = ""
    for line in file:       
        m = m + 1
        if n == m:
            row = line
            break
               
    file.close()
    if c in row:
        return True
    
    else:
        return False
        
        
    