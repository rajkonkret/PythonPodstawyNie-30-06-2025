class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """

        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h.")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmiana_biegu()

    def __zmiana_biegu(self):
        print("Zmiana abiegu")


sam = Car("VW", 2025)
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole prywatne, brak dostepu spoza klasy. tylko dedykowane metody
# print(sam.__predkosc)  # 50
sam.licznik()  # Prędkość wynosi: 50 km/h.
sam.__predkosc = 0
sam.licznik()  # Prędkość wynosi: 0 km/h. o le prywatne Prędkość wynosi: 50 km/h.
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.licznik()
# Prędkość wynosi: 0 km/h.
# Prędkość wynosi: 50 km/h.
# Zmian abiegu
# Zmian abiegu
# Zmian abiegu
# Zmian abiegu
# Zmian abiegu
# Prędkość wynosi: 0 km/h.
# hermetyzacja i wystawienie metod do odczytu i zapisu - enkapsulacja
