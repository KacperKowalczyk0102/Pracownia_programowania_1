# Zadanie 13

# 13. Napisz program obliczający wartości dla ułamków: 1/2, 1/3, ..., 1/10. Przykładowy wynik:

print("FOR")
for y in range(1, 11):
   print(f"1/{y} = {1/y}")

print("WHILE")
x = 1
while x<11:
    print(f"1/{x} = {1/x}")
    x+=1