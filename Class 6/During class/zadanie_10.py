# Zadanie 10

numbers = [15, 8, 31, 47, 2, 19]

def sum(numbers):
    suma = 0
    for n in numbers:
        suma += n
        
    return suma
    
    
def array2string(numbers):
    string = ""
    for n in numbers:        
        string += str(n)
        string += " "
        
    return string

print(f"Array: {array2string(numbers)}")
print(f"Sum of values: {sum(numbers)}")
    
    
     
        