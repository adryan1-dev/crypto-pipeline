from abc import ABC, abstractmethod
from typing import Dict,Any,List

class BaseCollector(ABC):
    def __init__(self, coin: List[str], fiat_coin: List[str]):
        self._coin = ','.join(coin)
        self._fiat_coin = ','.join(fiat_coin)

    @abstractmethod
    def fetch_data(self) -> List[Dict[str,Any]]:
        pass