# Zadanie 11

film_titles = ["Kevin sma w domu", "Władca Pierścieni", "Hobbit", "Ojciec chrzestny", "Zielona mila"]

file = open("files\movies.txt", "w")
for title in film_titles:
    file.write(title+"\n")
file.close()