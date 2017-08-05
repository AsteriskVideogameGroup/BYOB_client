from typing import Dict, List

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.gamecreationwaitstate import GameCreationWaitState
from view.viewmanager.machinestates.iclientstate import IClientState


class UnrankedModeSelectionState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

        self._currentselection: int = 0

    def input(self, messageinput: GameMessages, args: Dict[str, any] = None) -> IClientState:

        newstate: IClientState = None

        print("Ricevuto: {0}".format(args.get("mode")))

        newstate = GameCreationWaitState()

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, data: Dict[str, any] = None):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def run(self):
        print("Devi scegliere una modalità")

        self._viewcomposer.show(Templates.GAMESELECTION)
        print("Stai ancora scegliendo una modalità")



