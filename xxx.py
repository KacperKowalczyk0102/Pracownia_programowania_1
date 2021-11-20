folder = "Class 7"
# During class
for i in range(7, 13):
    file = open(folder+"\During class\zadanie_"+str(i)+".py", "x")
    file.close()
    
# After class
for i in range(13, 30):
    file = open(folder+"\After class\zadanie_"+str(i)+".py", "x")
    file.close()

