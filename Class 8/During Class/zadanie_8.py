# Zadanie 8

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

# a
print(person)

#b
print(person["name"])

# c
print(person["hobby"])

#d
person["surname"] = "Nowak"
print(person["surname"])

#e
#person["maried"] = not person["maried"]

#F
person["gender"] = "male"
print(person)


#g
person["hobby"].append("male")
print(person)

#h
