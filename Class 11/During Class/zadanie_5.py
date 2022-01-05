# Zadanie 5

class Song():

    def __init__(self, artist, track, title, year):
        self.artist = artist
        self.track = track
        self.title = title
        self.year = year

    def __str__(self):
        return "Performer:\t" + self.artist + "\nAlbum:\t\t" + self.track + "\nSong:\t\t" + self.title + "\nYear:\t\t" + self.year


s1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
print(s1)