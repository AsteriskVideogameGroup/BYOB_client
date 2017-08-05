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

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, **data: dict):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def input(self, messageinput: GameMessages, args: Dict[str, any]) -> IClientState:

        newstate: IClientState = None

        '''if messageinput == GameMessages.NEXT:
            self._currentselection = (self._currentselection + 1) % len(self._nextstates)
            print("Selezione: {0}".format(self._currentselection))

        elif messageinput == GameMessages.PREVIOUS:
            self._currentselection = (self._currentselection - 1) % len(self._nextstates)
            print("Selezione: {0}".format(self._currentselection))

        elif messageinput == GameMessages.ACCEPT:
            newstate = self._nextstates.get(self._currentselection)

        elif messageinput == GameMessages.EXITPROGRAM:
            print("sto uscendo")
            os._exit(1)  # TODO può essere migliorato, questo uccide tutti thread'''

        if messageinput == GameMessages.INITUNRANKEDGAME:
            newstate = UnrankedModeSelectionState()  # nuovo stato di selezione della modalità
        else:
            print("messaggio {0} sconosciujto".format(messageinput))

        return newstate

    def run(self):

        # visualizza il main menu
        self._viewcomposer.show(Templates.MAINMENU)
