import requests
from typing import Dict,List, Any

from BasePipeline import BaseCollector
class CoinCollector(BaseCollector):
    API_URL = "https://api.coinmarketcap.com/v3/coins/markets"
    API_KEY = "CG-Z8TRYAG3c8Fva7bLwJ9U4piQ"

def fetch_data(self) -> List[Dict[str,Any]]:
    print(f'-> Coletando dados da CoinGecko para {self._moedas_fiat.upper()}...')

    params = {
        'vs_currency': self._moedas_fiat,
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
        'ids': self._moedas
    }

    try:
        response = requests.get(self.API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Erro critico na requisicao: {e}')
        return []

if __name__ == '__main__':
    moedas_alvo =['bitcoin', 'ethereum', 'solana', 'dogecoin']
    moedas_fiat_alvo = ['usd']

    coletor = CoinCollector(moedas_alvo, moedas_fiat_alvo)

    dados_brutos= coletor.fetch_data()

    if dados_brutos:
        print('\n--- Dados coletados com sucesso! (Estrutura JSON) ---')
        import json
        print(json.dumps(dados_brutos[:3], indent=4))
    else:
        print('\nFalha na coleta. Verifique a conexão ou a API.')

