import abc
from typing import List

from model.gamemanageusecase.characters.bobdescription import BobDescription


class IBobDescriptionDAO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getByID(self, id: str) -> BobDescription:
        pass

    @abc.abstractmethod
    def save(self, description: BobDescription) -> BobDescription:
        pass

    @abc.abstractmethod
    def update(self, description: BobDescription) -> BobDescription:
        pass

    @abc.abstractmethod
    def getAll(self) -> List[BobDescription]:
        pass
