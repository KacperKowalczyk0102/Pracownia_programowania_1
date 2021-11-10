# Zadanie 12

numbers = [15,8,31,47,2,19]

existed = ""
reverse = ""

for n in numbers:
    existed += str(n) + " "
    
# 1 method
for n in reversed(numbers):
    continue
    
# 2 method
for n in numbers[::-1]:
    reverse += str(n) + " "
    
print(f"Existed array: {existed}")
print(f"Reverse array: {reverse}")
