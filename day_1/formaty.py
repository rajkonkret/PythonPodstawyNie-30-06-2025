user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  # <class 'float'> - float, zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.

# sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek)) # Witaj Tomek, masz teraz 39 lat.
# TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
# %f - float

print("Witaj %(user)s, jesteś %(user)s" % {"user": user})  # Witaj Tomek, jesteś Tomek
print("Witaj %(user)a, jesteś %(user)a" % {"user": user})  # Witaj 'Tomek', jesteś 'Tomek'

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3)  # Używamy wersji pythona 3.0
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4 zaokrągla do wyświetlania
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4 zaokrągla do wyświetlania

x = 3.8796
print(x)
y = round(x)  # 3.8796
print(f"{y=}")  # y=4
z = round(x, 2)
print(f"{z=}")  # z=3.88

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^25}")  # "          Tomek          "

liczba = 678098789951
print(liczba)
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 678,098,789,951
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 678_098_789_951
print(f"Nasza duża liczba {liczba:_}".replace("_", " "))  # Nasza duża liczba 678 098 789 951

liczba = 15_000_000_000_000
print(liczba)  # 15000000000000
print(type(liczba))  # <class 'int'>
