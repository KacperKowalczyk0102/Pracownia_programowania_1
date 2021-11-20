# Zadanie 20

file = open("files\\numbers.txt", "w")

for i in range(0, 51):
    file.write(str(i) + "\n")

file.close()