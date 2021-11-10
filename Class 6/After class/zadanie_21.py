# Zadanie 21

numbers = [4,36,12,28,9,44,5]

max1 = numbers[0]
for n in numbers:
    if n > max1:
        max1 = n

max2 = 0
for n in numbers:
    if n > max2 and n != max1:
        max2 = n

print(f"Array: {numbers}")
print(f"Result: {max2}")