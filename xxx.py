import os

# Folder names
folder = "Class 11"
during = "During Class"
after = "After Class"

os.mkdir(folder)
os.mkdir(os.path.join(folder, during))
os.mkdir(os.path.join(folder, after))

# During class
for i in range(4, 8):
    file = open(folder+"/"+during+"/zadanie_"+str(i)+".py", "x")
    file.close()
    
# After class
for i in range(8, 16):
    file = open(folder+"/"+after+"/zadanie_"+str(i)+".py", "x")
    file.close()

