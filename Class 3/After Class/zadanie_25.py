#Zadanie 25

operator = 0;
zakres = 0;
for x in range(10):
    if operator < 5:
        zakres += 1
        operator += 1
    else:
        zakres-=1
    for y in range(zakres):
        print("*", end="")
    print("\t")