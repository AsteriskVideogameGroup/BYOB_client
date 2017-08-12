from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO


class DAOFactory(IDAOAbstractFactory):
    def __init__(self):
        self._modedao: IModeDAO = None

    def getModeDAO(self) -> IModeDAO:
        return self._modedao

    def init(self):
        if self._modedao is not None:
            print("DAO factory ready")

    @property
    def modedao(self) -> IModeDAO:
        return self._modedao

    @modedao.setter
    def modedao(self, dao: IModeDAO):
        self._modedao = dao
