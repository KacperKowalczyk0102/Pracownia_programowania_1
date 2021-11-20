# Zadanie 12

file = open("files\shopping.txt", "a")

def add_product():
    product = input("Podaj nazwę produktu: ")
    
    if product != "":
        file.write(product+"\n")
        add_product()
    else:
        print("->Dodano produkty")
 
add_product()
file.close()