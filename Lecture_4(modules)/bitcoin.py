import json
import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number.")

try:
    result = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=3694fc4e7605dac5e11ddf80263976a9f1f890adb845bec033645b0d98c37a27')
    indicator = result.json()

    price = float(indicator["data"]["priceUsd"])
    bitcoin_price = bitcoins * price
    print(f"{bitcoin_price:,.4f}")
except requests.RequestException as e:
    sys.exit(f"Request failed: {e}")