import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

print(base_path)
print(base_path2)
# ops_example
# ops_example/D

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)  # usunięcie katalogu gdy istnieje

# tworzenie katalogów
base_path.mkdir()

path_b = base_path / "A" / "B"
path_c = base_path / "A" / "C"
path_d = base_path / "A" / "D"

# nie tworzy ścieżki, tylko katalog
# brak A powoduje, że  nie stworzy B
# path_b.mkdir() # FileNotFoundError: [Errno 2] No such file or directory: 'ops_example/A/B'

# musimy jawnie powiedzzieć, stwórz nadrzędne
path_b.mkdir(parents=True)
path_c.mkdir()  # C się stworzy bo A już istnieje

# tworzenie plików
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding='utf-8') as stream:
        stream.write(f"Jakaś treść pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)

# zmiana nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renamed.log')

# kopiowanie pliku
ex1 = path_d / 'ex1renamed.log'
docelowy = path_c
shutil.copy(ex1, docelowy)

# /Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_5/katalogi.py
path_win = "/Users/radoslawjaniak/PycharmProjects/PythonPodstawyNie-30-06-2025/day_5/katalogi.py"
path_win = "\\Users\\radoslawjaniak\\PycharmProjects\\PythonPodstawyNie-30-06-2025\\day_5\\katalogi.py"
path_win = r"\Users\radoslawjaniak\PycharmProjects\PythonPodstawyNie-30-06-2025\day_5\katalogi.py"
# r zapewwnia poprawne zbudowanie ścieżki np na windows

# ścieżka = "C:\\nowy_folder\\plik.txt"     # trzeba podwajać backslash
# ścieżka_raw = r"C:\nowy_folder\plik.txt"  # można użyć raw string
