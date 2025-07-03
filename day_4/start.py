import pakiet

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# print(pakiet.powitanie())
# po dodaniu w __all__ w init.py
# info jest jest widoczne w klasycznym imporciwe
pakiet.info()  # Jestem pakietem

from pakiet import fun1  # importuje plik fun1

fun1.powitanie()  # Witaj!!!

import pakiet.fun1 as pk

# as - alias
pk.powitanie()  # Witaj!!!
