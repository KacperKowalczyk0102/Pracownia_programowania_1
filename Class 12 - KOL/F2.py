import re

class C:    
    def __init__(self, ip):
        self.ip = ip
        
    def m(self):
        lst = self.ip.split(".")

        if len(lst) != 4:
            return False
        
        for x in lst:
            x = int(x)
            if x < 0 or x > 255:
                return False
        else:
            return True