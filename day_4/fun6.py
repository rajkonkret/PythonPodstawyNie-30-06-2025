# stworzyc funkcję obliczającą średnią

def liczby(*cyfry):  # dowolna ilość argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    count = len(cyfry)
    suma_p = sum(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia wynosi: {avg}")
        print(f"Średnia wynosi: {avg_p}")
    finally:
        print("Kolejny uczeń")


liczby()
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# ()
# Bład: division by zero
# Kolejny uczeń
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# Średnia wynosi: 4.5
# Kolejny uczeń

# ()
# Bład: division by zero
# Kolejny uczeń
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# Średnia wynosi: 4.5
# Średnia wynosi: 4.5
# Kolejny uczeń
