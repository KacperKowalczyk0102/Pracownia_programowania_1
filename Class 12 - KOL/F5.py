class C:
    def __init__(self,array):
        self.array = array
        
    def m(self):
        state = True
        for key, elem in enumerate(self.array):
            if key % 2 == 0:
                if elem % 2 != 0:
                    return False            
            if key % 2 != 0:
                if elem % 2 == 0:
                    return False
        else:
            return True