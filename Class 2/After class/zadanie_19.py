# Zad 19
print("Zadanie 19")

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))

p = (a+b+c)/2
wynik = (p*(p-a)*(p-b)*(p-c))**(0.5)

print("Pole trójkąta = ", wynik)