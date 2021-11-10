# Zadanie 17

array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

for a in array1:
    st = True
    for r in array2:
        if a == r:
            st = False

    if st == True:
        print(a)