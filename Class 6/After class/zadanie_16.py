# Zadanie 16

numbers = [12, 6, 4, 9, 3]

def stars(n):
    pattern = ""
    for i in range(n):
        pattern += "*"

    return pattern

for n in numbers:
    print(f"{n}: {stars(n)}")
