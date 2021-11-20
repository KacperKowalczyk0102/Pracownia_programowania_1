# Zadanie 8

file = open('files/countries.txt','r')
for num, line in enumerate(file):
  print(num, line, end="")
file.close()
