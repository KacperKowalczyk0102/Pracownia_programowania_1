# Zadanie 25

def minmax(array):
    maxx = array[0]
    minn = array[0]

    for n in array:
        if n > maxx:
            maxx = n
        if n < minn:
            minn = n

    return [minn, maxx]


array = [6,8,3,1,0,5,7]
print(f"Array: {array}")
print(f"Result: {minmax(array)}")
