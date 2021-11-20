# Zadanie 22
import random

file = open("files\power_numbers.txt", "w")

for i in range(10):
    txt = ""
    num = random.randint(1, 10)
    txt += str(num) + ", "
    txt += str(num**2) + ", "
    txt += str(num ** 3) + "\n"
    file.write(txt)
