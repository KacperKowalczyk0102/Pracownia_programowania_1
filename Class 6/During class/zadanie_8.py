# Zadanie 8

numbers = [-15, 8, -31, 47, -2, 19]

maxx = 0
minn = numbers[0]
for n in numbers:
    if n > maxx:
        maxx = n
    
    if n < minn:
        minn = n
      
print(minn)
print(maxx)

# Funkcje wbudowane
print(min(numbers))
print(max(numbers))
    