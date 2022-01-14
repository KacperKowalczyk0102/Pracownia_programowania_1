class C:    
    def __init__(self, calkowita):
        self.x = int(calkowita)
        
    def __str__(self):
        if self.x >= 0:
            return "*" * self.x
        else:
            return ""