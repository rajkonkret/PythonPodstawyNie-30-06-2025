import requests

# https://api.nbp.pl/

# https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/

# url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)
print(response.text)

data = response.json()
print(data)

# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '127/A/NBP/2025', 'effectiveDate': '2025-07-03', 'mid': 4.2634}]}

print(data['currency'])  # euro

print(data['rates'])  # [{'no': '127/A/NBP/2025', 'effectiveDate': '2025-07-03', 'mid': 4.2634}]
print(data['rates'][0])  # {'no': '127/A/NBP/2025', 'effectiveDate': '2025-07-03', 'mid': 4.2634}
print(data['rates'][0]['mid'])  # 4.2634
