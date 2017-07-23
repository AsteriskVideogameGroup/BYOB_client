from foundations.network.clienthandling.client import Client
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.oophelpers.singleton import SingletonMetaclass
from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler


class NetworkSendingAdapter(metaclass=SingletonMetaclass):
    def __init__(self):
        self._corbamanager: ICorbaManager = None

        ### TODO lettura da file
        self._matchmakinghandlerid = "matchmakinghandler"
        ###

        self._matchmakinghandler: MatchMakingHandler = None
        self._clientid: str = None
        self._client: Client = None


    def init(self, manager: ICorbaManager):
        self._corbamanager = manager
        self._matchmakinghandler = self._corbamanager.getFromSystem(self._matchmakinghandlerid)


    def register(self, client: Client):
        self._client = Client
        self.clientid = self._corbamanager.remotize(client)

    def makeNewGame(self, modeid: str, isranked: bool):
        self._matchmakinghandler.makeNewGame(self.clientid, modeid, isranked)
