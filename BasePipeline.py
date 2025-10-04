from abc import ABC, abstractmethod
from typing import Dict,Any,List

class BaseCollector(ABC):
    def __init__(self, moedas: List[str], moedas_fiat: List[str]):
        self._moedas = ','.join(moedas)
        self._moedas_fiat = ','.join(moedas_fiat)

        @abstractmethod
        def fetch_data(self) -> List[Dict[str,Any]]:
            pass