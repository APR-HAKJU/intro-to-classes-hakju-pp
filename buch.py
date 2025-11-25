# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:


- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""
class Book:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel = titel
        self.autor = autor
        self.seiten = int(seiten)
        self.gelesen = bool(gelesen)

book_1 = Book("Erebos", "Mark Zuckerberg", 800, 0)
book_2 = Book("Harry Potter", "J.K. Rowling", 350, 1)

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

print(f"Du hast das Buch gelesen: {book_1.gelesen}")
print(f"Du hast das Buch gelesen: {book_2.gelesen}")
