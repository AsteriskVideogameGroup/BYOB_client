from typing import Dict

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.state import State
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState


class ChooseBobState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None
        self._data: Dict[str, any] = None

    def run(self):
        self._viewcomposer.show(Templates.CHOOSEBOB)

    def setPreviousState(self, state: State):
        pass

    def giveData(self, data: Dict[str, any]):
        pass

    def input(self, messageinput: GameMessages, data: Dict[str, any] = None) -> IClientState:

        newstate: IClientState = None
        # TODO gestire cambiamenti di stato
        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver
