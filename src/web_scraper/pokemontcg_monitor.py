import requests

card_id = "xy1-1"  # Venusaur EX (for example)
url = f"https://api.pokemontcg.io/v2/cards/{card_id}"


resp = requests.get(url)
resp.raise_for_status()
data = resp.json()

# Inspect the card data
print(data)
