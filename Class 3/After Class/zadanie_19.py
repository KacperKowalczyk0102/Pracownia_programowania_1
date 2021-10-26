# Zadanie 19

# 20. Napisz program, który oblicza wiek psa na psie lata.
# Przez pierwsze dwa lata życie psa wynosi 10,5 lat ludzkich.
# Następnie każdy rok psa równa się 4 latom ludzkim. Przykładowy wynik:

wiek_psa = int(input("Podaj wiek psa: "))

wiek = 0
for i in range(1, wiek_psa+1):
    if i <=2:
        wiek += 10.5
    elif i > 2:
        wiek += 4

print(f"Wiek psa to {int(wiek)} lat ludzkich")


