import abc


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def update(self, input: str) -> 'State':
        pass