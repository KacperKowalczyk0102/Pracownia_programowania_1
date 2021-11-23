import os

# Folder names
folder = "Class 8"
during = "During Class"
after = "After Class"

# os.mkdir(folder)
os.mkdir(os.path.join(folder, during))
os.mkdir(os.path.join(folder, after))

# During class
for i in range(8, 15):
    file = open(folder+"/"+during+"/zadanie_"+str(i)+".py", "x")
    file.close()
    
# After class
for i in range(15, 22):
    file = open(folder+"/"+after+"/zadanie_"+str(i)+".py", "x")
    file.close()

