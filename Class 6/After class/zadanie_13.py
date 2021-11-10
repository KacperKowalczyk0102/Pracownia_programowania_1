# Zadanie 13

numbers = [8,2,5,1,9]
powers_list = ""
numbers_list = ""

for n in numbers:
    power = n **2
    powers_list += str(power) + " "
    numbers_list += str(n) + " "

print(f"Array: {numbers_list}")
print(f"2nd power: {powers_list}")

