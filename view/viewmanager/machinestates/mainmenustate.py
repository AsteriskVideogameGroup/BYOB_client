import os
from typing import List, Dict

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState
from view.viewmanager.machinestates.unrankedmodeselectionstate import UnrankedModeSelectionState


class MainMenuState(IClientState):

    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

        self._currentselection: int = 0  # indice di selezione del giocatore


    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def input(self, messageinput: GameMessages) -> IClientState:

        newstate: IClientState = None

        if messageinput == GameMessages.INITUNRANKEDGAME:
            newstate = UnrankedModeSelectionState()  # nuovo stato di selezione della modalità
        else:
            print("messaggio {0} sconosciujto".format(messageinput))

        return newstate

    def run(self):

        # visualizza il main menu
        self._viewcomposer.show(Templates.MAINMENU)

    def setPreviousState(self, state: IClientState):
        pass

    def giveData(self, data: Dict[str, any]):
        pass

