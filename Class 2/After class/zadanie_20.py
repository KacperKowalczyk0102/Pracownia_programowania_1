# Zad 20
print("Zadanie 20")

wzrost = int(input("Podaj swój wzrost w CM: "))
waga = int(input("Podaj swoja wagę w KG: "))

wzrost = wzrost/100
bmi = int(waga/(wzrost**2))

print("Twoje BMI: ", bmi)