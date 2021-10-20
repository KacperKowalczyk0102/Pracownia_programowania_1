# Zadanie 31

# 31. Napisz program wyświetlający 20 liczb całkowitych losowych z zakresu od 5 do 10.

import random

for i in range(20):
    print(random.randint(5, 10), end=" ")