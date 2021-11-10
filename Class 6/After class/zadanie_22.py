# Zadanie 22

numbers = [4,36,12,28,9,44,5]

minn = numbers[0]
maxx = numbers[0]

for n in numbers:
    if n > maxx:
        maxx = n

    if n < minn:
        minn = n

print(f"Array: {numbers}")
print(f"Result: {maxx-minn}")