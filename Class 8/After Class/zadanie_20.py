# Zadanie 20

import json

file = open("students.json", "r")
data = json.load(file)
file.close()

new = []
for x in data:
    row = {"name": x["name"], "surname": x["surname"], "student_ID": x["student_ID"]}
    new.append(row)

print(new)
with open("limited.json", "w") as nfile:
    json.dump(new, nfile, indent=4)

