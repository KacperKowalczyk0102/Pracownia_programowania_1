# F6
import random

def rand(x, y):
    v = random.randint(x, y)
    if v%2 == 0 and v%3 == 0:
        print(v)
    else:
        rand(x, y)

