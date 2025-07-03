from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opsująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, 'Lecę z szybkością', self.szybkosc)

    @abstractmethod  # dekorator oznaczajacy metodę jako abstrakcyjną
    def wydaj_oglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiązkowe wywołąnie

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_oglos(self):
        print("Ko ko ko ko")


class Orzel(Ptak):
    """
    Kalsa dziedziczy po Ptak
    """

    def wydaj_oglos(self):
        print("Kier kir kier")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_oglos'
# or1 = Ptak("Orzeł", 50)
# or1.latam()  # Tu Orzeł Lecę z szybkością 50
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.wydaj_oglos()  # Ko ko ko ko

or2 = Orzel("Bielik", 55)
or2.latam()
or2.wydaj_oglos()
# Tu Bielik Lecę z szybkością 55
# Kier kir kier

lista = [kur2, or2]

# polimorfizm - obiekty roóżnych klas zachowująsie w zakresie metody wydaj_odglos tak samo
for i in lista:
    i.wydaj_oglos()
# Ko ko ko ko
# Kier kir kier
