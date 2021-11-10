# Zadanie 6

# I sposób
def phone_keyboard_1():
    x = 1
    for i in range(3):
        for j in range(3):
            print(x, end=" ")
            x += 1
        print()
        
# II sposób
def phone_keyboard_2():
    for i in range(1, 10):
        print(i, end=" ")
        if(i%3 == 0):
           print()
        
phone_keyboard_1()
print()
phone_keyboard_2()