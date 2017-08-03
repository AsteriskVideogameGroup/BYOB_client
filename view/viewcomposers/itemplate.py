import abc
from typing import Callable

from foundations.oophelpers.observersubject import Subject
from foundations.sysmessages.gamemessages import GameMessages


class ITemplate(Subject):
    @abc.abstractmethod
    def initialize(self, screen: object, observercallback: Callable[[object, GameMessages], None]) -> 'ITemplate':
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
