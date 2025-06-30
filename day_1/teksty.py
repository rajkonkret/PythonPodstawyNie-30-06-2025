tekst = "Witaj Świecie"
print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>

# stringi s
# stringi są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
# """ Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

print(tekst)
# Witaj Świecie
# 01234567890... indeksowanie od 0

print(tekst[6])  # Ś

print(tekst.index("Ś"))  # indeks numer 6

print(tekst.count("i"))  # występuje 3

print(tekst.count("j", 0, 4))  # z prawej strony zbiór otwarty, 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# usnięcie białych spacji i spacji -> strip()
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>
# kod litery Ś w kodzie szesnastkowym, \x kod szesnastkowy
print(encode_s.decode("utf-8"))  # Witaj Świecie

imie = "Radek"
# f - string format - tekst sformatowany
tekst_format = f"Mam na imię {imie} i lubię pythona."
print(tekst_format)  # Mam na imię Radek i lubię pythona.

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - w to miejsce wstawia string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}".format(imie))  # Witaj Radek

print("Witaj", imie)  # Witaj Radek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

"""komentarz 
wielolinijkowy"""
