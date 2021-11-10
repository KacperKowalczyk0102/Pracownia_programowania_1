# Zadanie 14

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

length = len(names[0])
longest = 0
names_list = ""

for name in names:
    names_list += name + ", "
    if len(name) > length:
        length = len(name)
        longest = name

print(f"Names: {names_list}")
print(f"Longest name: {longest}")

