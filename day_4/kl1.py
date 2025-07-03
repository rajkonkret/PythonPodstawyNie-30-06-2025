# klasa - element programowania obiektowego
# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcje w klasie
# obiekt - instancja klasy
# klasa musi być zdeklarowana przed użyciem
# tworzenie obiektu klasy uruchmia metode __init__ w klasie
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase -> PEP8
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(self)
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")


print(Human.__doc__)  # wypisanie dokumentacji
# Klasa Human opisująca człowieka w pythonie

# pydoc -b - serwer dokumentacji

# cd day_4 - przejscie do katalogu day_4

# tworzenie obiektu klasy
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x10282ef90>

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# #
# None
# k

cz1.imie = "Radek"
cz1.wiek = 45
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 45
# m
cz1.powitanie()  # Nazywam się: Radek

cz2 = Human()
cz2.imie = "Agata"
cz2.wiek = 21
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Agata
# 21
# k
cz2.powitanie()  # Nazywam się: Agata
