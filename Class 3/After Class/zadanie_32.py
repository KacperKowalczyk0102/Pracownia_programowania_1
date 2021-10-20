# Zadanie 32

# 32. Napisz program wyświetlający kupon na loterię (numery od 1 do 49) w formacie jak poniżej.

nr = 1
for i in range(7):
    for j in range(7):
        print(nr+(7*j), end="\t")
    nr += 1
    print()