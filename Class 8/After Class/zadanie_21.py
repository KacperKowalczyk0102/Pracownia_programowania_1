# Zadanie 21

import json

print("Date: \t\t Buying Rate: \t Selling Rate:")
print("===============================================")

with open("euro.json", "r") as file:
    data = json.load(file)

for x in data:
    for y in data["rates"]:
        print(f"{y['effectiveDate']} \t {y['bid']} \t {y['ask']}")