import requests
from typing import Dict,List, Any

from base_pipeline import BaseCollector
class CoinCollector(BaseCollector):
    API_URL = "https://api.coingecko.com/api/v3/coins/markets"

    def fetch_data(self) -> List[Dict[str,Any]]:
        print(f'-> Coletando dados da CoinGecko para {self._fiat_coin.upper()}...')

        params = {
        'vs_currency': self._fiat_coin,
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
        'ids': self._coin
    }

        try:
            response = requests.get(self.API_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f'Erro critico na requisicao: {e}')
            return []

if __name__ == '__main__':
    coin_target =['bitcoin', 'ethereum', 'solana', 'dogecoin']
    fiat_coin_target = ['brl']

    collector = CoinCollector(coin_target, fiat_coin_target)

    brute_data = collector.fetch_data()

    if brute_data:
        print('\n--- Dados coletados com sucesso! (Estrutura JSON) ---')
        import json
        print(json.dumps(brute_data[:3], indent=4))
    else:
        print('\nFalha na coleta. Verifique a conexão ou a API.')

