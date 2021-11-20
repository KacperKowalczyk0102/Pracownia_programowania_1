# Zadanie 17

file = open("files\lorem.txt", "r")
content = file.read()
file.close()

copy = open("files\copy.txt", "w")
copy.write(content)
copy.close()

