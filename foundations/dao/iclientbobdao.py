import abc
from typing import List

from model.clientgamemanage.clientbob import ClientBob


class IClientBobDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAll(self) -> List[ClientBob]:
        pass
