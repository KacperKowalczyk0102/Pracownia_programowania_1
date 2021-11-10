# Zadanie 15

colors = ["red", "green", "blue", "yellow", "orange", "pink", "white", "black"]

content = ""
for color in colors:
    content += color + "\n"

file = open("answear_15.txt", "x")
file.write(content)
file.close()