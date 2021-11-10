# Zadanie 17

def ile_razy(tekst, litera):
    ile = 0
    for znak in tekst:
        if znak == litera:
            ile += 1

    print(f"Litera '{litera}' pojawia się w tekście {ile} razy")


tekst = "You never get a second chance to make a first impression"
litera = "e"
ile_razy(tekst, litera)
