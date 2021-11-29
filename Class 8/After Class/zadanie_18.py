# Zadanie 18

stos = []

x = 18

while x > 0:
    y = x %2
    x = x // 2
    stos.append(y)

for i in reversed(stos):
    print(i, end=" ")