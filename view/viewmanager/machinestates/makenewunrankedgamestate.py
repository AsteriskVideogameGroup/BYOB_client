from typing import Dict

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.machinestates.iclientstate import IClientState


class MakeNewUnrankedGameState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

        '''self._nextstates: Dict[callable] = {

            GameMessages.INITUNRANKEDGAME: lambda vcomposer, server :

        }'''

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def update(self, messageinput: GameMessages, infos: Dict[str, any] = None) -> IClientState:
        newstate: IClientState = None

        # TODO gestione stati successivi

        return newstate

    def run(self):
        print("questa è la logica dei make new game")
