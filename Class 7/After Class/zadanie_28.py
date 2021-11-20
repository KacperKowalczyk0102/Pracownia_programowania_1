# Zadanie 28
import re
import math

file = open("files/grades.txt", "r")
content = file.read()
file.close()
reg = "\d\.\d"

grades = re.findall(reg, content)
suma = 0
for x in grades:
    suma += float(x)

print(f"Średnia ocen: {round( ( suma / len(grades) ), 2)}")
