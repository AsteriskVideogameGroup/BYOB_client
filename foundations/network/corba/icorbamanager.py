import abc


class ICorbaManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init(self, nsaddress: str = "localhost", nsport: int = 9090):
        pass

    @abc.abstractmethod
    def remotize(self, obj: object, objname: str = None) -> str:
        pass

    @abc.abstractmethod
    def getFromSystem(self, objectid: str):
        pass