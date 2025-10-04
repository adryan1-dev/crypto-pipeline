import requests
import pandas as pd

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)
print(df.head())

df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
df = df.rename(columns={'current_price': 'Preço', 'market_cap': 'Market Cap', 'total_volume': 'Volume 24h', 'price_change_percentage_24h': '% 24h'})
