# Zadanie 16

from ebook import E_book

book1 = E_book("Alhemik", "Paulo Coelho", 250)
book1.open()
book1.status()
book1.read(80)
book1.status()
book1.close()
book1.read(20)

