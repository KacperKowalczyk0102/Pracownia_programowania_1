# 1 sposób
count = 0
for item in range(2 , 10, 2):
    print(item)
    count+=1
print(f"We have {count} even number")

print("\t")
# 2 Sposób
count = 0
for item in range(1 , 10):
    if item % 2 == 0:
        print(item)
        count+=1
print(f"We have {count} even number")