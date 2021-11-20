# Zadanie 24
import re

message = "Wtorek: 22C, Środa: 21C, Czwartek: 26C"
exp = "\d{2}"

temperatures = re.findall(exp, message)

suma = 0
lp = 0
for x in temperatures:
    suma += int(x)
    lp += 1

print(f"Srednia temperatura: {suma/lp}")


