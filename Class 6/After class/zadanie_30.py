# Zadanie 30

import random

def rand_elem(array):
    ran = random.randint(0,len(array)-1)
    return(array[ran])

array = [15,8,31,47,2,19]
print(f"Random numbers from {array}")
print(rand_elem(array))
print(rand_elem(array))
print(rand_elem(array))