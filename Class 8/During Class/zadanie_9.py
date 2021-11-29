# Zadanie 9

telefon = {
        "producent": "Samsung",
        "seria": "Galaxy",
        "rok": "2021",
        "gwarancja": "2 lata",
        "nowy": True,
        "funkcje": ["NFC", "WIFI", "Bluetooth"]
    }

for key, value in telefon.items():
    print(key, ': ', value)