# stworzyć funkcję kantor
# ma miec dwie wew funkcje usd, eur
# w zależności od parametru ma zwrócić odpowiednią funkcję

def kantor(waluta):
    def usd(kwota):
        return 4.1 * kwota

    def eur(kwota):
        return 4.2 * kwota

    if waluta == "usd":
        return usd  # zwracamy adres funkcji
    elif waluta == "eur":
        return eur
    else:
        return None


kantor_eur = kantor("eur")
print(kantor_eur(1000))

kantor_usd = kantor("usd")
print(kantor_usd(8900))
# 4200.0
# 36490.0
