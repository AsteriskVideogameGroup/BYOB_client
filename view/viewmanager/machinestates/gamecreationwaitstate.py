from typing import Dict

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.state import State
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState


class GameCreationWaitState(IClientState):

    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None
        self._data: Dict[str, any] = None

    def input(self, messageinput: GameMessages, data: Dict[str, any] = None) -> IClientState:
        newstate: IClientState = None

        # print("Ricevuto: {0}".format(args.get("mode")))

        #print(se)

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def run(self):
        print("Attendi che sia pronta la partita mod: {0}".format(self._data.get("mode")))

        # visualizzazione template
        self._viewcomposer.show(Templates.GAMEWAIT)

        selectedmode: str = self._data.get("mode")
        isranked: bool = self._data.get("isranked")

        print(selectedmode)
        print(isranked)

        # invio messaggio di make new game al server
        # TODO effettuare il make new game
        #self._server.makeNewGame(selectedmode, isranked)

    def setPreviousState(self, state: IClientState):
        pass

    def giveData(self, data: Dict[str, any]):
        self._data: Dict[str, any] = data
