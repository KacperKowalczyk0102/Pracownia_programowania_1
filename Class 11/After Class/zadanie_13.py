# Zadanie 13

import random

class Arrays:

    @staticmethod
    def create_same_array(elements, values):
        array1 = []
        for x in range(elements):
            array1.append(values)
        return array1


    @staticmethod
    def creata_random_array(elements, value_from, value_to):
        array2 = []
        for x in range(elements):
            ran = random.randint(value_from, value_to)
            array2.append(ran)
        return array2


    @staticmethod
    def calculate_range_array(array, value_from, value_to):
        lp = 0
        for x in array:
            if x in range(value_from, value_to+1):
                lp += 1
        return lp


a1 = Arrays.create_same_array(10,4)
print(a1)
a2 = Arrays.creata_random_array(20, 7, 8)
print(a2)
a3 = Arrays.calculate_range_array(a2, 7, 8)
print(a3)


