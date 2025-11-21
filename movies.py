# Programm, dass uns Informationen über Filme ausgibt

movie_1 = ["Horror", "It", 2017, 135]
movie_2 = ["Fantasy", "Harry Potter", 1997, 97]

print(f"Titel des Films: {movie_1[1]}")
print(f"Titel des Films: {movie_2[1]}")

class Movie: # Klasse = Bauplan für ein Thema
    def __init__(self, title, genre, duration, release_year): # Konstruktor -> Wird immer aufgerufen,
                        # wenn ein neues Objekt erstellt wird
        self.title = title
        self.genre = genre
        self.duration = duration
        self.release_year = release_year
        print("Neuer Film wurde erstellt")

"""movie_3 = Movie() #erstellt uns ein Objekt nach dem Bauplan "Movie"
movie_4 = Movie()
movie_5 = Movie()

movie_3.title = "Real Steel"
print(f"Titel des Films: {movie_3.title}")

movie_3.genre = "Action"
movie_3.duration = 120
movie_3.release_year = 2015

movie_4.title = "Top Gun Maverick"
print(f"Titel des Films: {movie_4.title}")

movie_4.genre = "Action"
movie_4.duration = 135
movie_4.release_year = 2024
"""
movie_6 = Movie(title="Dune: Awakening", genre="Sci-Fi", duration=180, release_year=2020)
print(f"Titel des Films: {movie_6.title}")

movie_7 = Movie(title="Barbie", genre="Drama", duration=125, release_year=2023)
print(f"{movie_7.title} wurde im Jahr {movie_7.release_year} herausgebracht.")

