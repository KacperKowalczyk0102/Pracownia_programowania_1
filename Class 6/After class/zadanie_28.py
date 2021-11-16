# Zadanie 28

array = [897, 65, 14, 2, 78, 150, 240, 123]

line = "-"
content = "|"
for n in array:
    line += "-"* ( len( str(n) )+4 )
    content += "   "+str(n)+"|"

print(line)
print(content)
print(line)

