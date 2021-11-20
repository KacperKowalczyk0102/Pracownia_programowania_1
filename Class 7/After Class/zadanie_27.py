# Zadanie 27
import re

file = open("files/lorem.txt", "r")
text = file.read()
file.close()
reg = "\w+"

words = re.findall(reg, text)

for word in words:
    if len(word) >= 6:
        print(f"{word} \t {len(word)}")