import abc
from typing import List

from model.gamemanage.clientbobdescription import ClientBobDescription


class IClientBobDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAll(self) -> List[ClientBobDescription]:
        pass
