# Gegeben ist eine Liste, die Informationen über verschiedene Songs enthält.
# Verändere den Code so, dass eine Klasse "Song" definiert wird.
# Die Eigenschaften Titel, Künstler und Anzahl der Streams sollen als Attribute im Konstruktor definiert werden

class Song:
    def __init__(self, titel, Künstler, Anzahl_Streams):
        self.titel = titel
        self.künstler = Künstler
        self.anzahl_streams = int(Anzahl_Streams)
    
    def print_info(self):
        print(f"Der Song {self.titel} von {self.künstler} hat {self.anzahl_streams} Streams.")
        
song_1 = Song("Blinding Lights", "The Weeknd", 4_200_000_000)
song_2 = Song("Shape of You", "Ed Sheeran", 5_300_000_000)
song_3 = Song("Dance Monkey", "Tones and I", 3_400_000_000)

songs = [song_1, song_2, song_3]

#TODO: Aufgabe 1: 
#   Definiere die Klasse "Song" mit einem Konstruktor (__init__),
#  der die Attribute titel, künstler und streams initialisiert.

# TODO: Aufgabe 2:
#   Erstelle drei Objekte der Klasse "Song" mit den Informationen aus der Liste oben

# TODO: Aufgabe 3:
#   Gib für jeden Song den Titel und die Anzahl der Streams in folgendem Format aus:
#   "Der Song '<Titel>' von <Künstler> hat <Anzahl der Streams> Streams."

"""print(f"Der Song {song_1.titel} von {song_1.künstler} hat {song_1.anzahl_streams} Streams.")
print(f"Der Song {song_2.titel} von {song_2.künstler} hat {song_2.anzahl_streams} Streams.")
print(f"Der Song {song_3.titel} von {song_3.künstler} hat {song_3.anzahl_streams} Streams.")"""

for x in songs:
    x.print_info()