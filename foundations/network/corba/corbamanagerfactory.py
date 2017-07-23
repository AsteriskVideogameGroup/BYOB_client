from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.corba.pyrocorbamanager import PyroCorbaManager
from foundations.oophelpers.singleton import SingletonMetaclass


class CorbaManagerFactory(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._corbamanager: ICorbaManager = None

    def getCorbaManager(self) -> ICorbaManager:
        self._corbamanager = PyroCorbaManager()
        self._corbamanager.init()  # TODO l'inizializzazione deve essere fatta da file di conf

        return self._corbamanager
