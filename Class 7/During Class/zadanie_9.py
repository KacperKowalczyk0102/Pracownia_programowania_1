# Zadanie 9

file = open('files\liczby.txt','r')

suma = 0
for num in file:
    suma += int(num)
file.close()
print(suma)

    