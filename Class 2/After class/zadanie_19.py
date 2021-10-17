# Zad 19
print("Zadanie 19")

a = int(input("Podaj długoścboku a: "))
b = int(input("Podaj długoścboku b: "))
c = int(input("Podaj długoścboku c: "))

p = (a+b+c)/2
wynik = (p*(p-a)(p-b)(p-c))**(0.5)

print("Pole trójkąta = ", int(wynik))