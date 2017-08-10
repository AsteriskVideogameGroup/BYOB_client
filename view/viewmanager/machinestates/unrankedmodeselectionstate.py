from typing import Dict, List

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from model.clientgamemanage.clientmode import ClientMode
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

    def input(self, messageinput: GameMessages, data: Dict[str, any] = None) -> IClientState:
        newstate: IClientState = None

        if messageinput == GameMessages.UNRANKEDMODESELECTED:
            newstate = GameCreationWaitState()
            data["isranked"] = False
            newstate.giveData(data)
        elif messageinput == GameMessages.PREVIOUS:
            newstate = self._previousstate

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def run(self):
        print("Devi scegliere una modalità")

        self._viewcomposer.show(Templates.GAMESELECTION)

        # TODO prendere da file!!!
        mod1: ClientMode = ClientMode()
        mod1.id = "classic_mode"
        mod1.name = "classic_mode"
        mod1.dimensions = (5, 5)
        mod1.duration = 5
        mod1.numplayers = 4

        mod2: ClientMode = ClientMode()
        mod2.id = "mod2"
        mod2.name = "modalità2"
        mod2.dimensions = (75, 7)
        mod2.duration = 200
        mod2.numplayers = 2

        mod3: ClientMode = ClientMode()
        mod3.id = "mod3"
        mod3.name = "modalità3"
        mod3.dimensions = (8, 7)
        mod3.duration = 700
        mod3.numplayers = 4

        # TODO prendere da file
        args: Dict[str, any] = {
            "ranked": False,
            "modes": [mod1, mod2, mod3]
        }

        self._viewcomposer.setAssets(args)

        print("Stai ancora scegliendo una modalità")

    def setPreviousState(self, state: IClientState):
        self._previousstate = state

    def giveData(self, data: Dict[str, any]):
        pass
