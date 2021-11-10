# Zadanie 26

numbers = [15,8,31,47,2,19]

parzyste = []
nieparzyste = []

for n in numbers:
    if n % 2 == 0:
        parzyste.append(n)
    else:
        nieparzyste.append(n)

result = []
for i in parzyste:
    result.append(i)

for j in nieparzyste:
    result.append(j)

print(result)




