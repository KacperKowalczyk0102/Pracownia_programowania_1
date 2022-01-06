class C:
    def __init__(self, tekst):
        self.tekst = tekst

    def m(self):
        state = True
        for x in range(len(self.tekst)):
            for y in range(x+1, len(self.tekst)):
                if self.tekst[x] == self.tekst[y]:
                    state = False

        return state

