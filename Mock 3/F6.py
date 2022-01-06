class C:
    def __init__(self, array):
        self.array = array

    def m(self):
        lp = 0
        for x in range(1, len(self.array)-1):
            if self.array[x-1] != self.array[x] and self.array[x+1] != self.array[x]:
                lp += 1
        return lp