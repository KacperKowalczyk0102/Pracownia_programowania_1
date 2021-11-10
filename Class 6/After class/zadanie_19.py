# Zadanie 19

numbers = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = ""

for n in numbers:

    st = True
    for m in numbers:
        if n == m:
            st = False

    if st == True:
        print(str(n) + " ")

# print(unique_elements)
