import abc

from foundations.dao.iclientbobdao import IClientBobDAO
from foundations.dao.imodedao import IModeDAO


class IDAOAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init(self):
        pass

    '''@abc.abstractmethod
    def getPlayerDAO(self) -> IPlayerDAO:
        pass'''

    @abc.abstractmethod
    def getModeDAO(self) -> IModeDAO:
        pass

    @abc.abstractmethod
    def getClientBobDAO(self) -> IClientBobDAO:
        pass
        # TODO bisogna mettere la gestione dei descrittori dei bob
