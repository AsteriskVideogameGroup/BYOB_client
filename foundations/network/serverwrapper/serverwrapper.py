from typing import Callable, Dict

from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.oophelpers.singleton import SingletonMetaclass
from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.sysmessages.gamemessages import GameMessages


class ServerWrapper(metaclass=SingletonMetaclass):
    def __init__(self):
        self._corbamanagerfactory: CorbaManagerFactory = None
        self._matchmakinghandlerid: str = None
        self._matchmakinghandler: MatchMakingHandler = None
        self._client: Client = None

    def init(self):
        self._matchmakinghandler = self._corbamanagerfactory.getCorbaManager().getFromSystem(self._matchmakinghandlerid)

    def registerClient(self, client: Client):
        self._client: Client = client
        self._client.clientid = self._corbamanagerfactory.getCorbaManager().remotize(client)

    def addListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        if self._client is not None:
            self._client.registerEventListener(callback)

    def makeNewGame(self, modeid: str, isranked: bool):
        print(self._client.clientid)
        self._matchmakinghandler.makeNewGame(self._client.clientid, modeid, isranked)

    @property
    def matchmakinghandlerid(self) -> str:
        return self._matchmakinghandlerid

    @matchmakinghandlerid.setter
    def matchmakinghandlerid(self, identifier: str):
        self._matchmakinghandlerid = identifier

    @property
    def corbamanagerfactory(self) -> CorbaManagerFactory:
        return self._corbamanagerfactory

    @corbamanagerfactory.setter
    def corbamanagerfactory(self, manager: CorbaManagerFactory):
        self._corbamanagerfactory = manager

