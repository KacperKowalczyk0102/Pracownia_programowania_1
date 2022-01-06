class C:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def m(self):
        try:
            return int(self.dictionary["value"], int(self.dictionary["system"]))
        except:
            return -1