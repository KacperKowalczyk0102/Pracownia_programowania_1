# Zadanie 18

numbers = [5,9,7,6,4,2,1,85,95,14,75,32,55]

def bubblesort(numbers):
    n = len(numbers)

    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if numbers[l] > numbers[l + 1]:
                numbers[l], numbers[l + 1] = numbers[l + 1], numbers[l]
                zamien = True

        n -= 1
        if zamien == False: break

    return numbers

print(f"Nieposortowane: {numbers}")
print(f"Posortowane:  {bubblesort(numbers)}")