# Zadanie 7

numbers = [1, 6, 7, 3, 9, 6, 3, 8]

parzyste = 0
nieparzyste = 0

for n in numbers:
    if n % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1
        

print(f"Parzyste: {parzyste}")
print(f"Nieparzyste: {nieparzyste}")