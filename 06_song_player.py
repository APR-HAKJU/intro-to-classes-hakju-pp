"""
Übung 4: Klassen importieren & Datentypen verstehen

Aufgabe:
In dieser Übung lernst du:
1. Wie man Klassen aus anderen Dateien importiert
2. Dass Klassen eigene Datentypen sind

Schritte:
1. Importiere die Klasse Song aus dem File 05_song.py
2. Erstelle mehrere Song-Objekte mit Titeln und Interpreten deiner Wahl
3. Verwende type() um zu zeigen, dass jedes Objekt vom Typ 'Song' ist
4. Vergleiche mit anderen Datentypen (String, Integer, Liste)

💡 Tipps:
- from dateiname import Klassenname importiert eine Klasse
- type(variable) gibt den Datentyp zurück
- Jede Klasse ist ein eigener Datentyp!
- Du kannst beliebige Songs, Titel und Interpreten verwenden!

Beispiel Ergebnis:
=== Datentypen Vergleich ===
Text: <class 'str'>
Zahl: <class 'int'>
Liste: <class 'list'>
Song1: <class '__main__.Song'>
Song2: <class '__main__.Song'>

Beide Songs haben denselben Datentyp: True

=== Song Playlist ===
▶️ Song 'Summer Vibes' wird gespielt...
▶️ Song 'Neon Lights' wird gespielt...
▶️ Song 'Ocean Wave' wird gespielt...
"""

# TODO: Importiere die Klasse Song aus 05_song
# from 05_song import Song
from song import Song #from "filename ohne py" import "Classname"
song_1 = Song("Africa", "Toto", "https://www.youtube.com/watch?v=FTQbiNvZqaY&list=RDFTQbiNvZqaY&start_radio=1")
song_1.zeige_info()
song_2 = Song("Africa", "Toto", "https://www.youtube.com/watch?v=FTQbiNvZqaY&list=RDFTQbiNvZqaY&start_radio=1")

# TODO: Erstelle verschiedene Variablen mit unterschiedlichen Datentypen
# text = "Hallo"
# zahl = 42
# liste = [1, 2, 3]
text = "Hallo"
zahl = 42
liste = [1, 2, 3]

print(type(text))
print(type(zahl))
print(type(liste))
print(type(song_1))
#Immer wenn eine neue Klasse angelegt wird, wird ein neuer Datentyp erstellt.

liste_songs = [song_1, song_2]
print(liste_songs[0].titel)
print(liste_songs[0].zeige_info())
print(liste_songs[0].interpreten)
print(liste_songs[1].titel)
print(liste_songs[1].zeige_info())
print(liste_songs[1].interpreten)

song_3 = Song("Fein", "Travis Scott", "df")
liste_songs.append(song_3)

for x in liste_songs:
    print(x.titel)

# TODO: Erstelle 3 Song-Objekte mit Titeln und Interpreten deiner Wahl


# TODO: Zeige die Datentypen mit type()
# print("=== Datentypen Vergleich ===")
# print(f"Text: {type(text)}")
# print(f"Zahl: {type(zahl)}")
# print(f"Liste: {type(liste)}")
# print(f"Song1: {type(song1)}")
# print(f"Song2: {type(song2)}")
# print()


# TODO: Vergleiche, ob zwei Songs denselben Datentyp haben
# print(f"Beide Songs haben denselben Datentyp: {type(song1) == type(song2)}")
# print()


# TODO: Spiele alle Songs ab
# print("=== Song Playlist ===")
