# Zadanie 18

# 19. Są monety o nominale 1, 2 i 5 polskich złotych (PLN).
# Napisz program pokazujący dowolną ilość (liczbę naturalną)
# odczytaną z klawiatury przy jak najmniejszej liczbie monet.

amount = int(input("Podaj wartość: "))

piec = 0
dwa = 0
jeden = 0

while amount > 0:
    if amount >= 5:
        amount -= 5
        piec += 1
        continue
    elif amount >= 2:
        amount -= 2
        dwa =+ 1
        continue
    else:
        amount -= 1
        jeden += 1
        continue

print(f"5 zł - {piec}")
print(f"2 zł - {dwa}")
print(f"1 zł - {jeden}")

