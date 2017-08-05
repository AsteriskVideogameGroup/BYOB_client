import abc
from typing import Callable

from foundations.sysmessages.gamemessages import GameMessages


class Subject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def registerEventListener(self, callback: Callable[[object, GameMessages, any], None]):
        pass

    @abc.abstractmethod
    def detachEventListerners(self, callback: Callable[[object, GameMessages, any], None]):
        pass


