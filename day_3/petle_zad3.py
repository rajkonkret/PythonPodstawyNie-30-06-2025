# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat !")

licznik = 0
while True:
    licznik += 1
    print("Kmunikat 2 !!!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

licznik = 0
print(45 * "-")
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Kmunikat 2 !!!
# 11
# ---------------------------------------------
# Komunikat 3 !!!
#
# password = input("Podaj hasło")
# while password != "secret":  # != różne,
#     password = input("Podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłoadsadfsaf
# Podaj ponownieasdasfsd
# Podaj ponownieassdasfaf
# Podaj ponownieaDAFG
# Podaj ponownieSECRET
# Podaj ponowniesecret
# Hasło prawidłowe

# ctrl / - komentowanie

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    # A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break

    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5', '6']
print(lista_int)  # [1, 2, 3, 4, 5, 6]
