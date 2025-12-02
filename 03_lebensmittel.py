"""
Übung 3: Einkaufswagen

Aufgabe:
Erstelle zwei Klassen:
1. Artikel: Repräsentiert einen einzelnen Artikel mit Name und Preis
2. Einkaufswagen: Verwaltet eine Liste von Artikel-Objekten

Der Einkaufswagen soll:
- Artikel hinzufügen können
- Den Gesamtpreis berechnen
- Die Anzahl der Artikel zählen
- Den Inhalt anzeigen
"""

# TODO 1: Erstelle die Klasse Artikel mit passendem Konstruktor
class Artikel:
    def __init__(self, name, preis):
        self.name = str(name)
        self.preis = float(preis)
    def zeige_info(self):
        print(f"Name: {self.name}")
        print(f"Preis: {self.preis}")
    """
    Ein einzelner Artikel im Einkaufswagen.
    
    Attribute:
    - name (str): Name des Artikels
    - preis (float): Preis des Artikels
    """
    # TODO 1.1: Schreibe den Konstruktor __init__
    # Parameter: self, name, preis
    # Speichere name und preis als Attribute
    pass
    
    # TODO 1.2: Schreibe die Methode zeige_info()
    # Gibt aus: "- {name}: {preis} EUR"
    pass


# TODO 2: Erstelle die Klasse Einkaufswagen
class Einkaufswagen:
    def __init__(self):
        self.artikel = []
    def hinzufuegen(self, artikel):
        self.artikel.append(artikel)
        print(f"Der Artikel {artikel} wurde hinzugefügt.")
    def gesamtpreis(self):
        summe = 0
        for x in self.artikel:
            summe += x.preis
        return summe
    def anzahl_artikel(self):
        print(len(self.artikel))
    def zeige_inhalt(self):
        print(f"Einkaufswagen {self.anzahl_artikel} Artikel:")
        for x in self.artikel:
            x.zeige_info()
    """
    Ein Einkaufswagen der Artikel-Objekte verwaltet.
    
    Attribute:
    - artikel (list): Liste von Artikel-Objekten
    """
    
    # TODO 2.1: Schreibe den Konstruktor __init__
    # Keine Parameter außer self
    # Initialisiere eine leere Liste self.artikel = []
    pass
    
    # TODO 2.2: Schreibe die Methode hinzufuegen(artikel)
    # Parameter: self, artikel (ein Artikel-Objekt)
    # Füge das Artikel-Objekt zur Liste hinzu
    # Gib aus: "✅ {artikel.name} hinzugefügt"
    pass
    
    # TODO 2.3: Schreibe die Methode gesamtpreis()
    # Keine Parameter außer self
    # Berechne die Summe aller Preise (artikel.preis)
    # Gib die Summe zurück (return)
    pass
    
    # TODO 2.4: Schreibe die Methode anzahl_artikel()
    # Keine Parameter außer self
    # Gib die Anzahl der Artikel zurück (len(self.artikel))
    pass
    
    # TODO 2.5: Schreibe die Methode zeige_inhalt()
    # Keine Parameter außer self
    # Gib aus: "Einkaufswagen ({anzahl} Artikel):"
    # Für jeden Artikel: Rufe artikel.zeige_info() auf
    # Gib aus: "Gesamtpreis: {gesamtpreis} EUR"
    pass


# TODO 3.1: Erstelle drei Artikel-Objekte
# artikel1 = Artikel("Brot", 2.99)
# artikel2 = Artikel("Milch", 1.49)
# artikel3 = Artikel("Käse", 4.50)
pass
artikel1 = Artikel("Brot", 2.99)
artikel2 = Artikel("Milch", 1.49)
artikel3 = Artikel("Käse", 4.50)

# TODO 3.2: Erstelle einen Einkaufswagen
# wagen = Einkaufswagen()
pass
wagen = Einkaufswagen()
# TODO 3.3: Füge die drei Artikel zum Wagen hinzu
# wagen.hinzufuegen(artikel1)
# wagen.hinzufuegen(artikel2)
# wagen.hinzufuegen(artikel3)
pass
wagen.hinzufuegen(artikel1)
wagen.hinzufuegen(artikel2)
wagen.hinzufuegen(artikel3)
# TODO 3.4: Zeige den Inhalt des Wagens
wagen.zeige_inhalt()



"""
Erwartetes Ergebnis:
✅ Brot hinzugefügt
✅ Milch hinzugefügt
✅ Käse hinzugefügt

Einkaufswagen (3 Artikel):
- Brot: 2.99 EUR
- Milch: 1.49 EUR
- Käse: 4.50 EUR
Gesamtpreis: 8.98 EUR
"""
