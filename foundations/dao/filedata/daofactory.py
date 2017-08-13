from foundations.dao.iclientbobdao import IClientBobDAO
from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO


class DAOFactory(IDAOAbstractFactory):
    def __init__(self):
        self._modedao: IModeDAO = None
        self._clientbobdao: IClientBobDAO = None

    def getModeDAO(self) -> IModeDAO:
        return self._modedao

    def getClientBobDAO(self) -> IClientBobDAO:
        return self._modedao

    def init(self):
        if self._modedao is not None:
            print("DAO factory ready")
        if self._modedao is not None:
            print("DAO factory ready")

    @property
    def modedao(self) -> IModeDAO:
        return self._modedao

    @modedao.setter
    def modedao(self, dao: IModeDAO):
        self._modedao = dao

    @property
    def clientbobdao(self) -> IClientBobDAO:
        return self._clientbobdao

    @modedao.setter
    def clientbobdao(self, dao: IClientBobDAO):
        self._clientbobdao = dao
