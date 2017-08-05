from typing import Dict, List

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState


class UnrankedModeSelectionState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

        self._currentselection: int = 0

        # TODO leggere da file
        self._modes: List[str] = [

            "classic",
            "hardcore",
            "destructive"

        ]

    def input(self, messageinput: GameMessages, args: Dict[str, any]) -> IClientState:

        newstate: IClientState = None

        if messageinput == GameMessages.NEXT:
            self._currentselection = (self._currentselection + 1) % len(self._modes)
            print("Selezione: {0}".format(self._currentselection))

        elif messageinput == GameMessages.PREVIOUS:
            self._currentselection = (self._currentselection - 1) % len(self._modes)
            print("Selezione: {0}".format(self._currentselection))

        elif messageinput == GameMessages.ACCEPT:
            print("Modalità scelta: {0}".format(self._modes[self._currentselection]))
            # newstate = self._modes.get(self._currentselection)
        else:
            print("messaggio {0} sconosciujto".format(messageinput))

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, **data: dict):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def run(self):
        print("Devi scegliere una modalità")

        self._viewcomposer.show(Templates.GAMESELECTION)
        print("Stai ancora scegliendo una modalità")

        # self._server.makeNewGame()


