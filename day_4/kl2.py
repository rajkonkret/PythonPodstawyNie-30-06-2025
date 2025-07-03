class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(self)
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    # wypisz_wiek, wypisz_wzrost
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Agata", 21, 170)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)

cz1.powitanie()  # Nazywam się: Agata
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Nazywam się: Agata
# Mam 21 lat.
# Mam 170 cm wzrostu.

cz1.ruszaj()  # Ruszyłam w drogę

cz2 = Human("Radek", 45, 190, "m")
cz2.ruszaj()
cz2.wypisz_wiek()
# Ruszyłem w drogę
# Mam 45 lat.
