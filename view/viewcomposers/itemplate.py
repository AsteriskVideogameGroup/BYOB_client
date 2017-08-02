import abc
from typing import Callable, Dict

import pygame

from foundations.sysmessages.gamemessages import GameMessages


class ITemplate(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize(self, screen: object, observercallback: Callable[[object, GameMessages, Dict[str, any]], None]):
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
