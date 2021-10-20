#Zadanie 26

# 26. Karta płatnicza zabezpieczona jest czterocyfrowym kodem PIN (0805).
# Napisz program sprawdzający poprawność wprowadzonego w terminalu płatniczym kodu PIN.
# Użytkownik ma do trzech możliwości wprowadzenia kodu PIN.
# W przypadku trzech nieudanych prób karta zostaje zablokowana.

good_pin = 1234
    
for i in range(3):
    pin = int(input("Podaj kod PIN: "))
    if pin == good_pin:
        print("Prawidłowy PIN")
        break
    else:
        print("Niepoprawny PIN ...")
        if i==2:
            print("Twoja karta płatnicza została zablokowana!")
    
        

