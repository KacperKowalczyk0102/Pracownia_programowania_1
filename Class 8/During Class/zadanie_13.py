# Zadanie 13

import json

with open("json_file.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)
