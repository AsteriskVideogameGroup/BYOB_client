from threading import Thread
from typing import List, Callable, Dict

import Pyro4

from foundations.oophelpers.observersubject import Subject
from foundations.sysmessages.gamemessages import GameMessages


@Pyro4.expose
class Client(Subject):
    """# eventi che può lanciare il proxy
    MAPREADYEVENT: str = "mapready"
    GAMEREADYEVENT: str = "gameready\""""

    def __init__(self):
        #self._userid: str = userid
        self._clientid: str = None

        self._gamehandlerid: str = None

        # self._eventlisteners: dict = dict()

        self._eventlisteners: List[Callable[[object, GameMessages, Dict[str, any]], None]] = list()

    @property
    def clientid(self) -> str:
        return self._clientid

    @clientid.setter
    def clientid(self, value: str):
        self._clientid = value

    '''@property
    def playerid(self) -> str:
        return self._userid

    @playerid.setter
    def playerid(self, value: str):
        self._userid = value'''

    @property
    def gamehandler(self) -> str:
        return self._gamehandlerid

    @gamehandler.setter
    def gamehandler(self, gamehandleid: str):
        self._gamehandlerid = gamehandleid

    def notifyGameReady(self, gamehandlerid: str):
        self.gamehandler = gamehandlerid
        self._notify(GameMessages.MAPREADY)

    def notifyMapReady(self):
        self._notify(GameMessages.GAMECREATED)

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlisteners.remove(callback)

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlisteners.append(callback)

    def _notify(self, message: GameMessages):

        def threadrun(*args):
            operation: callable = args[0]
            operation(message)

        for callback in self._eventlisteners:
            callback: callable
            Thread(target=threadrun, args=(callback, None)).run()
