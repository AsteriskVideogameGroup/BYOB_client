import abc


class ITemplate(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initialize(self, screen: IScreen):
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
