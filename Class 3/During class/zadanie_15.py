# Zadanie 15

# 15. Poniższy program oblicza sumę liczb całkowitych z zakresu od 1 do 5. Uruchom program w trybie debugowania i znajdź błąd.

sum = 0
number = 1
while number < 6:
  sum = sum + number
  number = number + 1
print("Sum of numbers in <1,5> is ", sum)