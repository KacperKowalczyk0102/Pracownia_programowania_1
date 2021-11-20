# Zadanie 21
import random

file = open("files/random_numbers.txt", "w")

for i in range(0, 51):
    file.write(str(random.randint(100, 999)) + "\n")

file.close()

