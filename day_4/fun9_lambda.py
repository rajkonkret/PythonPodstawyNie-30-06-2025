# funkcja lambda
# skrócony zapis funkcji
# domyslnie ma return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(5, 89))  # -84

odejmij2 = lambda a, b: a - b
print(odejmij2(7, 90))  # -83

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(15))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły


