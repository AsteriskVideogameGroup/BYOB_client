import abc
from typing import Dict

from foundations.sysmessages.gamemessages import GameMessages


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def input(self, messageinput: GameMessages, args: Dict[str, any] = None) -> 'State':
        pass
