class C:
    def __init__(self, names):
        self.names = names

    def m(self):
        state = False
        for x in range(len(self.names)):
            for y in range(x+1, len(self.names)):
                if self.names[x] == self.names[y] or self.names[x] == self.names[y].upper():
                    state = True
        return state

