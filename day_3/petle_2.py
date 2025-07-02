dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))

# wyswietli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wwyświetlenie wartości
for i in dictionary.values():
    print(i)

# wyswietlenie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski


for k, v in dictionary.items():
    print(k, v, sep="=>", end="<==>")

# imie=>Radek<==>nazwisko=>Kowalski<==>
print("Radek")
# imie=>Radek<==>nazwisko=>Kowalski<==>Radek
print("Tomek")
# imie=>Radek<==>nazwisko=>Kowalski<==>Radek
# Tomek

pol_ang = {'kot': "cat", 'pies': "dog", 'dach': "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

# print({k: v for k, v in pol_ang.items() if k != "kot"})
# {'pies': 'dog', 'dach': 'roof'}
# zrób pętle po słowniku
for k, v in pol_ang.items():
    if k != "kot":
        print(k, v)

# zrob petle posłowniku i wypisz pary
for k, v in pol_ang.items():
    print(k, "=>", v)
# dach roof
# kot => cat
# pies => dog
# dach => roof
# wypisz pary i oddziel znakiem ()
for k, v in pol_ang.items():
    print(f"({k}, {v})", end=" ")

print("Tomek")
# tabnine, coopilot
