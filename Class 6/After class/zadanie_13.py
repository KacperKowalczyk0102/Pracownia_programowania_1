# Zadanie 13

numbers = [8,2,5,1,9]
powers_list = ""
numbers_list = ""

for n in numbers:
    power = n **2
    powers_list += str(power) + " "

print(f"Array: {numbers}")
print(f"2nd power: {powers_list}")

