import chardet

# pip install chardet
with open('test.log', "r", encoding="utf-8") as f:
    raw_data = f.read()

print(raw_data)

# "rb" - odczyt bajtowy - wymaga tak biblioteka chardet
with open('test.log', "rb") as f:
    raw_data = f.read()

print(raw_data)
# b'Powitanie\nKolejne\njescze jedno\nPowitanie\nDopisane\nDo\xc5\x9bpisane\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.6271830985915493, 'language': ''}
# po zwiększeniu próbki (więcej polskich liter w pliku)
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}

encoding = result['encoding']
confidence = result['confidence']

print("Kodowaie:", encoding)  # Kodowaie: utf-8
print("Trafność:", confidence)  # Trafność: 0.938125

print(raw_data.decode(encoding=encoding))
# Powitanie
# Kolejne
# jescze jedno
# Powitanie
# Dopisane
# Dośćąźpisane