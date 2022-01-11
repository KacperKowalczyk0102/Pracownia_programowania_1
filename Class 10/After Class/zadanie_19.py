# Zadanie 19

class Statistics:

    def __init__(self):
        self.number = []
        self.small = 0
        self.great = 0
        self.arithmetic = 0
        self.median = 0


    def add_number(self):
        number = int(input("Give a number: "))
        self.number.append(number)


    def display(self):
        print("Numbers: ", end="")
        for x in self.number:
            print(x, end=", ")
        print()


    def greatest(self):
        maxn = self.number[0]
        for i in self.number:
            if i > maxn:
                maxn = i
        self.great = maxn


    def smallest(self):
        minn = self.number[0]
        for i in self.number:
            if i > minn:
                minn = i
        self.small = minn


    def arithmetic_mean(self):
        suma = 0
        for i in self.number:
            suma = suma + i

        self.arithmetic= round(suma/len(self.number), 2)


    def mediana(self):
        print(len(self.number))
        if len(self.number) % 2 == 0:
            x = int(len(self.number)/2)
            y = int(len(self.number)/2)-1
            self.median = (self.number[x] + self.number[y])/2
        else:
            x = int(len(self.number)/2)
            self.median = self.number[x]


    def results(self):
        print("Results: ")
        print(f"\tSmallest: {self.small}")
        print(f"\tGreatest: { self.great}")
        print(f"\tArithmetic mean: {self.arithmetic}")
        print(f"\tMedian: {self.median}")


s1 = Statistics()
s1.add_number()
s1.add_number()
s1.add_number()
s1.add_number()
s1.display()
s1.smallest()
s1.greatest()
s1.arithmetic_mean()
s1.mediana()
s1.results()