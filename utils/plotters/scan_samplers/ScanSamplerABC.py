from abc import ABC, abstractmethod

from classes.db_models import ScanDB


class ScanSamplerABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return f"Плоттер типа: {self.__class__.__name__}"

    @abstractmethod
    def do_sampling(self, scan: ScanDB):
        pass
