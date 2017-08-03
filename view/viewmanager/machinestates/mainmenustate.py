import os
from typing import Dict

import sys

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.machinestates.iclientstate import IClientState
from view.viewmanager.machinestates.makenewunrankedgamestate import MakeNewUnrankedGameState


class MainMenuState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def input(self, messageinput: GameMessages) -> IClientState:
        ''''''  # TODO manca un' eventuale logica di update

        newstate: IClientState = None

        if messageinput == GameMessages.NEXT:
            print("ho ricevuto il messaggio next")

        if messageinput == GameMessages.PREVIOUS:
            print("ho ricevuto il messaggio prev")

        elif messageinput == GameMessages.EXITPROGRAM:
            print("sto uscendo")
            os._exit(1)  # TODO può essere migliorato, questo uccide tutti thread
        else:
            print("messaggio {0} sconosciujto".format(messageinput))

        return newstate

    def run(self):
        print("logica di main menu state")
