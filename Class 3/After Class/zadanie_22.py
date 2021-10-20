# Zadanie 22

# 23. Napisz program, który wyświetla liczby od 1 do 30. Jeśli liczba jest podzielna przez 3, to program wyświetla słowo 'THREE'.
# Następnie, jeśli liczba jest podzielna przez 5, program wyświetla słowo „PIĘĆ”.
# Wreszcie, jeśli liczba jest podzielna przez 3 i 5, program wyświetla słowo „BINGO”.

for number in range(1,31):
    print(number, end=" | ")
    if  number%3 == 0 and  number%5 == 0:
        print("BINGO", end="")
    else:
        if number%3 == 0:
            print("TRZY", end="")
        if number%5 == 0:
          print("PIĘĆ", end="")
    print()
