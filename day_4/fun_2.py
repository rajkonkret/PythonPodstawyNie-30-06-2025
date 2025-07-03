# zoom

# funkcje zwracające wynik
# kończy się słówkiem return

def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(6, 90))  # 96
wynik = dodaj(89, 76)
print("Wynik:", wynik)  # Wynik: 165

# uruchomic na kilka sposobów te funkcje
print(odejmij(6, 8, 9))  # -11
print(odejmij(1, c=8))  # -7
print(odejmij(a=90))  # 90

print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 15))  # 1150.0
print(oblicz_vat(vat=8, kwota=6789))  # 7332.12

zm = oblicz_vat(1000) # 1241.0

if zm == 1230:
    print("Ok")  # Ok

print(dodaj(5, 6) + oblicz_vat(1000))
