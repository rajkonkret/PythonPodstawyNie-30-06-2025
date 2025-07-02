# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# warunek musi zwracac typ bool
# Indent Rainbow

odp = True
print(bool(odp))  # True

odp = False
if odp:
    # blok programu wykonywany gdy warunek spęłniony
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
print(bool(odp))  # True
if odp:
    print("Dane zostały odebrane")
    # Dane zostały odebrane

if odp == "Radek":
    print("Nadal Radek")
    # Nadal Radek

odp = 0  # -> False
print(bool(odp))  # rzutowanie na typ logiczny

if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Dlugość wynosi {len(a)}, więcej niż 3")
    # Dlugość wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
    # Dlugość wynosi 5, więcej niż 3

# walrus operator, operator mors :=
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
    # Długość wynosi 5, więcej niż 3

# podatek = 0
# zarobki = int(input("Podaj zarobki"))

# # działą tylko pierwszy spełniony
# # kolejnośc warunków ma znaczenie
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln")
# # 0.2 dla przedziału 10_000 do 39_999
# # Podaj zarobki50000
# # Podatek wynosi 20000.0 pln

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulejemy sytem zbierania logów
# zmienna bedzie przechowywac informację jaki system przysłał log
# email, console, inny
# console -> "Stało się coś strasznego"
# email -> "System email"
# jesli system email to do listy błędó∑ dopisac opis błędu
# error -> Krytyczny itd...
alert_system = "email"
error = "medium"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:  # inny warunek
    print("Inny system")

print("Lista błędów:", lista_b)
# Lista błędów: ['Ostrzeżenie']

# napisac test z...
# 3 pytania
# dodac punktację
punkty = 0

odp = input("Podaj rok Chrztu Polski")
if odp.strip().casefold() == '966':
    punkty += 1  # punkty = punkty + 1
    print("Prawidłowa odpowiedż")
else:
    print("Idż się pouczyć")

odp = input("Podaj stolicę Polski")
if odp.strip().casefold() == "Warszawa".casefold():
    punkty += 1  # punkty = punkty + 1
    print("Prawidłowa odpowiedż")
else:
    print("Idż się pouczyć")

print(f"Otrzymujesz: {punkty} pkt.")

# Podaj rok Chrztu Polski966
# Prawidłowa odpowiedż
# Podaj stolicę PolskiWarszawa
# Prawidłowa odpowiedż
# Otrzymujesz: 2 pkt.
# #
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
