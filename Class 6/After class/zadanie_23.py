# Zadanie 23

# a
arrayA = [1,0,9,4,6]
# b
arrayB = [6,8,3,1,0,5,7]

def median(numbers):

    # Sorotwanie bąbelkowe
    n = len(numbers)

    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if numbers[l] > numbers[l + 1]:
                numbers[l], numbers[l + 1] = numbers[l + 1], numbers[l]
                zamien = True

        n -= 1
        if zamien == False: break

    # Znajdowanie mediany
    if len(numbers) % 2 != 0:
        result = numbers[len(numbers) // 2]
    else:
        result = ( numbers[(len(numbers) // 2)] + numbers[(len(numbers) // 2)+1] )/2

    return result


print(median(arrayA))
print(median(arrayB))

