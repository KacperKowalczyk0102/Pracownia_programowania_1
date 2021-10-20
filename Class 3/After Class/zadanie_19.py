# Zadanie 19

# 20. Napisz program, który oblicza wiek psa na psie lata.
# Przez pierwsze dwa lata życie psa wynosi 10,5 lat ludzkich.
# Następnie każdy rok psa równa się 4 latom ludzkim. Przykładowy wynik:

wiek_psa = int(input("Podaj wiek psa: "))

if wiek_psa <= 2:
    print("Wiek psa to 10,5 lat ludzkich")
else:
    wiek = 10.5
    wiek += (wiek_psa-2) * 4
    print(f"Wiek psa to {wiek} lat ludzkich")


