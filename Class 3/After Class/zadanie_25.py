#Zadanie 25

# 25. Zmienne aib zawierają wymiary boków prostokąta.
# Napisz program, który utworzy następujący prostokąt o wymiarach a i b.
# Przykładowy wynik dla a = 4 i b = 15:

a = 4
b = 15

for x in range(a):
    for y in range(b):
        if x == 0 or x == (a-1):
            print("*", end="")
        else:
            if y == 0 or y == (b-1):
                print("*", end="")
            else:
                print(" ", end="")
    print()