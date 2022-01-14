import json

class C:
    def __init__(self):
        file = open("data.json")
        self.data = json.load(file)
        file.close()
        
    def m(self, n1, n2 ,n3):
        lp = 0
        for x in self.data:
            age = x["husband"]["age"]
            children = len(x["children"])
            
            if age > n1 and age < n2 and children >= n3:
                lp += 1
        return lp