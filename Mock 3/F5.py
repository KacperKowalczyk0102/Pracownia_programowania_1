class C:
    def __init__(self, t):
        self.t = t

    def m1(self):
        dictionary = {}
        letters = []
        for x in self.t:
            letters.append(x)
        list(dict.fromkeys(letters))

        for y in letters:
            lp = 0
            for z in self.t:
                if z == y:
                    lp += 1
            dictionary[y] = lp

        return dictionary


    def m2(self, c1):
        dictionary = {}
        for y in c1:
            lp = 0
            for z in self.t:
                if z == y:
                    lp += 1
            dictionary[y] = lp

        return dictionary