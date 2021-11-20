# Zadanie 18

file = open("files\lorem.txt", "r")
copy = open("files\copylines.txt", "w")

for line in file:
    copy.write(line)

file.close()
copy.close()

