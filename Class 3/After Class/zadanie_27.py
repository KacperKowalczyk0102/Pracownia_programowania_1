# Zadanie 27

# 27. Komputerowa klawiatura numeryczna ma układ klawiszy jak poniżej.
# Dołączony kod programu wyświetla klawiaturę komputera.
# Przeanalizuj program pod kątem wyświetlanych wyników.
# Czy rozumiesz każdą instrukcję programu?
# Następnie dokonaj zmiany w kodzie programu. Zastąp wyrażenie „for” wyrażeniem „while”.

print()
print("FOR")

for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()


print()
print("WHILE")

x = 6
while x>(-1):
    y = 1
    while y<4:
        print(f' {x+y}',end='')
        y += 1
    x -= 3
    print()
