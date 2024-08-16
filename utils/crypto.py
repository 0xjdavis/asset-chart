import requests
import json
from datetime import datetime, timedelta

def get_crypto_historical_data(crypto_id, days):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    parameters = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data

# Number of days of historical data to retrieve
days = 7

# Fetch historical data
bitcoin_data = get_crypto_historical_data('btcusd', days)
ethereum_data = get_crypto_historical_data('ethusd', days)

# Combine data into a single dictionary
crypto_data = {
    'bitcoin': bitcoin_data,
    'ethereum': ethereum_data
}

# Save the data to a JSON file
output_file = 'crypto_price_history.json'
with open(output_file, 'w') as file:
    json.dump(crypto_data, file, indent=4)

print(f"Crypto price history saved to {output_file}")
