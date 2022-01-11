import json

class C:
    def __init__(self):
        file = open("mockdata.json")
        self.j = json.load(file)
        file.close()

    def m1(self, n1, n2):
        lp = 0
        for x in self.j:
            if x["wife"]["age"] >= n1 and len(x["children"]) >= n2:
                lp += 1
        return lp

    def m2(self, n1):
        families = []
        for x in self.j:
            if len(x["children"]) >= n1:
                families.append(x)
        file = open("mockdata1.json", "w")
        json.dump(families, file, indent=4)
        file.close()
        return families

