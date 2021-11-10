# Zadanie 10

def read_number():
    liczba = int(input("Wprowadź liczbę: "))
    return liczba

#x = read_number()
#y = read_number()
#print(f"SUMA: {x+y}")

print(f"SUMA: {read_number()+read_number()}")