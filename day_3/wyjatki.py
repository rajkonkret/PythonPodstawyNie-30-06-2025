# wyjątki - błędy w działaniu programu

# print(5 / 0)
# /Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/.venv/bin/python /Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_3/wyjatki.py
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_3/wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

lista = []
try:
    # print(5 / 0)
    # print("A" * "23")
    # print(lista[10])
    # raise KeyError("Brak klucza")  # rzucamy wyjątek
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except Exception as e:  # złapie pozostałe wyjatki
    print("Bład:", e)
else:  # wykona się gdy nie ma błędu
    print("wynik:", wynik)
finally:  # wykona się zawsze
    print("Kolejne obliczenie")

print("Program nadal działa!")

# Nie dziel przez zero
# Program nadal działa!
# Bład typu
# Program nadal działa!
# Bład: 'Brak klucza'
# Program nadal działa!
# wynik: 2.727272727272727
# Program nadal działa!
# wynik: 2.727272727272727
# Kolejne obliczenie
# Program nadal działa!
