# działania z plikami
# filehanler = rura do pliku
# context manager - ułatwia pracę z plikami
# with

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("jescze jedno\n")

# "x" - rzuca bład gdy plik istnieje
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x",  encoding="utf-8") as f:
#     f.write("Powitanie")

# "w" - kasuje plik gdy istnieje, tworzy nowy
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("jescze jedno\n")

# "a" dodanie do istniejącego pliku
with open("test.log", "a", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Dopisane\n")
    fh.write("Dośćąźpisane\n")

# "r" odczyt
with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# Powitanie
# Kolejne
# jescze jedno
# Powitanie
# Dopisane
# Dopisane
