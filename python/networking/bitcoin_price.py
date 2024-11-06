import requests
import json
url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bpi']['USD']['rate']
    print(f"Current Bitcoin Price: {bitcoin_price} USD")
else:
    print("Failed to retrieve Bitcoin price.")
