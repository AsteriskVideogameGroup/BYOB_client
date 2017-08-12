import abc
from typing import List

from model.clientgamemanage.clientmode import ClientMode


class IModeDAO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getByID(self, id: str) -> ClientMode:
        pass

    @abc.abstractmethod
    def save(self, mode: ClientMode) -> ClientMode:
        pass

    @abc.abstractmethod
    def update(self, mode: ClientMode) -> ClientMode:
        pass

    @abc.abstractmethod
    def getAll(self) -> List[ClientMode]:
        pass
