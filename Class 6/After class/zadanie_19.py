# Zadanie 19

numbers = [3, 3, 2, 5, 8, 1, 9, 8, 8, 9]
unique_elements = ""
not_elements = []

for pos, val in enumerate(numbers):
    if pos < len(numbers)-1 and (val in not_elements) == False:
        temp = numbers[pos+1::]
        if (val in temp) == False:
            unique_elements += str(val) + ", "
        else:
            not_elements.append(val)

print(f"Array: {numbers}")
print(f"Unique elements: {unique_elements}")
