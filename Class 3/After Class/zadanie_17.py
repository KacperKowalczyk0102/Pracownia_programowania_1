# Zadanie 17

# 18. Niech x i y oznaczają współrzędne punktu na płaszczyźnie.
# Napisz program, który określa, w którym kwadrancie układu współrzędnych znajduje się punkt P (x, y)
# lub na której osi się znajduje, lub że znajduje się w pozycji (0,0) układu współrzędnych.

x = float(input("Podaj X: "))
y = float(input("Podaj Y: "))

if x==0 and y==0:
    print("Punkt leży w środku układu współrzędnych")
    print(f"({x}, {y})")
elif x==0 or y==0:
    if x==0 and y!=0:
        print("Punkt leży na osi Y")
        print(f"({x}, {y})")
    elif y==0 and x!=0:
        print("Punkt leży na osi X")
        print(f"({x}, {y})")
else:
    if x>0 and y>0:
        print("I ćwiartka układu")
        print(f"({x}, {y})")
    elif x>0 and y<0:
        print("II ćwiartka układu")
        print(f"({x}, {y})")
    elif x<0 and y<0:
        print("III ćwiartka układu")
        print(f"({x}, {y})")
    elif x<0 and y>0:
        print("IV ćwiartka układu")
        print(f"({x}, {y})")