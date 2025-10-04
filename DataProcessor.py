import pandas as pd
from typing import List, Dict,Any, Union
from CoinCollector import CoinCollector

class DataProcessor:
    def __init__(self, brute_data: List[Dict[str,Any]]):
        self._brute_data = brute_data
        self.df = None

    def _variation_format(self, variable: Union[float, int]) -> str:
        if pd.isna(variable) or variable == 0:
            return f'⚫ 0.00%'
        elif variable > 0:
            return f"🟢 +{variable:,.2f}%"
        else:
            return f"🔴 {variable:,.2f}%"

    def process_and_analysis(self) -> pd.DataFrame:
        if not self._brute_data:
            print('Dados brutos vazios. Processamento cancelado.')
            return pd.DataFrame()

        self.df = pd.DataFrame(self._brute_data)

        self.df.rename(columns={
            'current_price': 'Preço',
            'total_volume': 'Volume_24h',
            'price_change_percentage_24h': 'Variacao_24h',
        }, inplace=True)

        self.df['status_variacao'] = self.df['Variacao_24h'].apply(self._variation_format)
        self.df['Preço'] = self.df['Preço'].round(2)

        print('\nDados processados e prontos para exibição.')
        return self.df [['name', 'symbol', 'Preço', 'Volume_24h', 'status_variacao']]

if __name__ == '__main__':
    print('--- INICIANDO TESTE DA PIPELINE ---')
    coin_target = ['bitcoin', 'ethereum', 'solana', 'dogecoin']
    fiat_coin_target = ['usd']

    collector = CoinCollector(coin_target, fiat_coin_target)
    brute_data = collector.fetch_data()

    if brute_data:
        processor = DataProcessor(brute_data)
        df_final = processor.process_and_analysis()
        print('\n--- Resultado Final (Data Frame Processado) ---')
        print(df_final.to_string())
    else:
        print('\nFalha na coleta. Verifique a conexão ou a API.')
