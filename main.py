import requests

valor = float(input("Digite o valor em BRL: "))
moeda = input("Converter para (USD, EUR, GBP): ").upper()

r = requests.get("https://open.er-api.com/v6/latest/BRL").json()
taxa = r["rates"].get(moeda)

if taxa:
    print(f"{valor:.2f} BRL = {valor*taxa:.2f} {moeda}")
else:
    print("Moeda não suportada.")
