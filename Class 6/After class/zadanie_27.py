# Zadanie 27

def array2string(numbers):
    string = ""
    for n in numbers:
        string += str(n) +", "
    return string

numbers = [15,8,31,47,2,19]
print(f"Array: {numbers}")
print(f"String: {array2string(numbers)}")


