# od python 3.10
# match case

lista = []
lang = input("Podaj znany Ci jezyk programowania")

match lang.strip().casefold():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append('Znam Jave')
    case _:  # else, wartość domyślna
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci jezyk programowaniapython
# ['Znam Pythona']
# odaj znany Ci jezyk programowaniac++
# Nie znam takiego języka
# []
