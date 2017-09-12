import abc


class LibraryImporter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getClassObject(self, classname: str, modulename: str) -> object:
        pass