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

        self._previousstate: IClientState = None

    def input(self, messageinput: GameMessages) -> IClientState:
        newstate: IClientState = None

        if messageinput == GameMessages.MODESELECTED:
            newstate = GameCreationWaitState()
        elif messageinput == GameMessages.PREVIOUS:
            newstate = self._previousstate

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def run(self):
        print("Devi scegliere una modalità")

        self._viewcomposer.show(Templates.GAMESELECTION)
        print("Stai ancora scegliendo una modalità")

    def setPreviousState(self, state: IClientState):
        self._previousstate = state

    def giveData(self, data: Dict[str, any]):
        pass
