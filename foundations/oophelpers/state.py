import abc

from foundations.sysmessages.gamemessages import GameMessages


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def update(self, input: GameMessages) -> 'State':
        pass
