import abc
from typing import Dict


class InjectionSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getContent(self) -> Dict[str, Dict[str, any]]:
        pass


