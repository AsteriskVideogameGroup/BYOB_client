import abc
from typing import Callable


class ITemplate(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize(self, screen: IScreen, observercallback: Callable[[str], None]):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    @abc.abstractmethod
    def getInputs(self):
        pass

    @abc.abstractmethod
    def setAssets(self, **kwargs: dict):
        pass
