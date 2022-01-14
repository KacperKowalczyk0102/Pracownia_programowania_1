class C:
    def __init__(self, tekst):
        self.tekst = tekst
        
    def m(self):
        letters = []
        for a in self.tekst:
            if a in letters:
                continue            
            letters.append(a)
        
        obj = {}
        for b in letters:
            lp = 0
            for c in self.tekst:
                if c == b:
                    lp += 1
            obj[b] = lp
        
        return(obj)