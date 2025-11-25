# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer

haus1 = Haus(3, 2, 5)

"""haus1.quadratmeter = 120
haus1.schlafzimmer = 3
haus1.badezimmer = 2"""

print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.

haus2 = Haus(5, 5, 3)
haus3 = Haus(80, 7, 1)
haus4 = Haus(23, 3, 4)

# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.

print(f"Anzahl der Schlafzimmer: {haus1.schlafzimmer}; Anzahl der Badezimmer: {haus1.badezimmer}")
print(f"Anzahl der Schlafzimmer: {haus2.schlafzimmer}; Anzahl der Badezimmer: {haus2.badezimmer}")
print(f"Anzahl der Schlafzimmer: {haus3.schlafzimmer}; Anzahl der Badezimmer: {haus3.badezimmer}")
print(f"Anzahl der Schlafzimmer: {haus4.schlafzimmer}; Anzahl der Badezimmer: {haus4.badezimmer}")