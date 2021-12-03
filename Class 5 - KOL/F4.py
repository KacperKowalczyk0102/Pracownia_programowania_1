# F4

def f4(n1, n2, n3):
    najm = 0
    najw = 0
    
    # Wszystkie liczby takie same
    if n1 == n2 and n2 == n3 and n1 == n3:
        return "Brak"
    else:
        # Dwie takie same liczby
        if n1 == n2:
            if n2 > n3:
                najw = n2
            elif n3 > n2:
                najw = n3
            
            if n2 < n3:
                najm = n2
            elif n3 < n2:
                najm = n3
                
        elif n2 == n3:
            if n1 > n3:
                najw = n1
            elif n3 > n1:
                najw = n3
            
            if n1 < n3:
                najm = n1
            elif n3 < n1:
                najm = n3
                
        elif n3 == n1:
            if n2 > n1:
                najw = n2
            elif n1 > n2:
                najw = n1
            
            if n2 < n1:
                najm = n2
            elif n1 < n2:
                najm = n1
            
        # Każda liczba inna
        else:
            if n1 > n2 and n1 > n3:
                najw = n1
            elif n2 > n3 and n2 > n1:
                najw = n2
            elif n3 > n2 and n3 > n1:
                najw = n3
                
            if n1 < n2 and n1 < n3:
                najm = n1
            elif n2 < n3 and n2 < n1:
                najm = n2
            elif n3 < n2 and n3 < n1:
                najm = n3
            
        roznica = najw - najm
        return roznica
        
    