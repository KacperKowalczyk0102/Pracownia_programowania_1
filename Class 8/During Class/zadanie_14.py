# Zadanie 14

import json

movie = {
        "title": "Forrest Gump",
        "year": "1994",
        "director": "Robert Zemeckis",
        "category": "drama/comedy",
        "time": "142min",
        "country": "USA"
        }

with open('favourite.json', 'w') as file:
    json.dump(movie, file, indent=4)