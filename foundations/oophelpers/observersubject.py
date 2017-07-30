import abc
from collections import Callable


class Subject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def registerEventListener(self, callback: callable):
        pass

    @abc.abstractmethod
    def detachEventListerners(self, callback: callable):
        pass


