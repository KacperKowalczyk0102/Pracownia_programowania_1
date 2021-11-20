# Zadanie 19

lista1 = open("files\ZiarnaIChleb.txt", "r")
lista2 = open("files\MiesoIRyby.txt", "r")

shoppinglist = open("files\shoppinglist.txt", "w")
shoppinglist.write(lista1.read())
shoppinglist.write(lista2.read())
