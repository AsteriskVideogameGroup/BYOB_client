import abc
from typing import Callable, Dict

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.templates import Templates


class IViewComposer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, eventlistener: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    @abc.abstractmethod
    def show(self, chosenview: Templates):
        pass

    @abc.abstractmethod
    def setAssets(self, kwargs: Dict[str, any]):
        pass

    @abc.abstractmethod
    def startWorking(self):
        pass

