import abc


class IDependencyInjectionContainer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init(self, configpath: str):
        pass

    @abc.abstractmethod
    def getObject(self, id: str) -> object:
        pass
