class C:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def m(self):
        for key, elem in enumerate(self.numbers):
            for key2, elem2 in enumerate(self.numbers):
                if key2 == key:
                    continue
                else:
                    if elem2 == elem:
                        return True
        return False