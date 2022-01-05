# Student 12

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_in_row(array):
        for c in array:
            if c == array[-1]:
                print(c)
            else:
                print(f"{c},", end=" ")


my_array = [4, 1, 8, 7, 2]
Arrays.print_in_row(my_array)
