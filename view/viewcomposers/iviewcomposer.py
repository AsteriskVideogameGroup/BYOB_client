import abc
from typing import Callable

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.viewsnames import ViewNames


class IViewComposer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, eventlistener: Callable[[object, GameMessages], None]):
        pass

    @abc.abstractmethod
    def show(self, chosenview: ViewNames):
        pass

    @abc.abstractmethod
    def setAssets(self, **kwargs):
        pass

