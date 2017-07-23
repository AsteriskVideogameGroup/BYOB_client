from threading import Thread

import Pyro4

from foundations.oophelpers.observersubject import Subject


@Pyro4.expose
class Client(Subject):

    # eventi che può lanciare il proxy
    MAPREADYEVENT: str = "mapready"
    GAMEREADYEVENT: str = "gameready"

    def __init__(self, clientid: str, userid: str):
        self._clientid: str = clientid
        self._userid: str = userid

        self._gamehandlerid: str = None

        self._eventlisteners: dict = dict()

    @property
    def clientid(self) -> str:
        return self._clientid

    @property
    def playerid(self) -> str:
        return self._userid

    @property
    def gamehandler(self) -> str:
        return self._gamehandlerid

    @gamehandler.setter
    def gamehandler(self, gamehandleid: str):
        self._gamehandlerid = gamehandleid

    def notifyGameReady(self, gamehandlerid: str):
        self.gamehandler = gamehandlerid
        self._notify(Client.GAMEREADYEVENT)

    def notifyMapReady(self):
        self._notify(Client.MAPREADYEVENT)

    def detachEventListerners(self, eventid: str):
        self._eventlisteners.pop(eventid)

    def registerEventListener(self, eventid: str, callback: callable):
        self._eventlisteners[eventid] = callback

    def _notify(self, event: str):

        def threadrun(*args):
            this = args[0]
            operation: callable = args[1]
            operation(this)

        callback: callable = self._eventlisteners.get(event)
        Thread(target=threadrun, args=(self, callback)).run()
