import abc
from typing import List

from model.clientgamemanage.clientmode import ClientMode


class IModeDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAll(self) -> List[ClientMode]:
        pass
