# Zadanie 9

# 9. Użytkownik wprowadza z klawiatury dwie liczby całkowite.
# Napisz program, który sprawdza, czy przynajmniej jeden z nich jest pozytywny.

liczba1 = int(input("Enter first number: "))
liczba2 = int(input("Enter second number: "))

if liczba1 > 0 and liczba2 > 0:
    print("Both numbers are positive")
elif liczba1 > 0 and liczba2 < 0:
    print("First number is positive")
elif liczba1 < 0 and liczba2 > 0:
    print("Second number is positive")
else:
    print("Both numbers are negative")
