# F6

import json

def f6(c, n):
    with open("students.json", "r") as file:
        data = json.load(file)
    
    lp = 0
    for x in data["students"]:
        if ( x["country"] == c ) and ( len(x["languages"]) >= n ):
            lp = lp + 1
    
    return lp
            
        
    