import abc


class DataSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def open(self, uri: str):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def getURI(self) -> str:
        pass
    