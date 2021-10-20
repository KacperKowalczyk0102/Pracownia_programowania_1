# Zadanie 16

# 16. Napisz program wyświetlający dwie liczby wprowadzane z klawiatury w kolejności rosnącej.

liczba1 = int(input("Enter first number: "))
liczba2 = int(input("Enter second number: "))

if liczba1 > liczba2:
    print(f"Numbers in ascending order: {liczba2} , {liczba1}")
elif liczba2 > liczba1:
    print(f"Numbers in ascending order: {liczba1} , {liczba2}")
else:
    print(f"Numbers in ascending order: {liczba1} , {liczba2}")