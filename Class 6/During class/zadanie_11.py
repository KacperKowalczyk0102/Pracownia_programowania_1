# Zadanie 11

# a
array1a = ["water","book","sky"]  
array2a = ["water","book","sky"] 

#b
array1b = [True, False]
array2b = [True, False, True]

#c
array1c = [5,3,1]
array2c = [5,3,1]

#d
array1d = [3,2,1]
array2d = [3,2]

# e
array1e = ["water","book","sky"]  
array2e = ["water","book","winter"] 

def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(l1):
            if array1[i] != array2[i]:
                return False
            return True
    else:
        return False

print(compare(array1a, array2a))
print(compare(array1b, array2b))
print(compare(array1c, array2c))
print(compare(array1d, array2d))
print(compare(array1e, array2e))
        
    