import os
from typing import List, Dict

from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState


class TempSecondaIterazioneState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, daofactory: IDAOAbstractFactory):
        self._viewcomposer = viewmanager
        self._server = gameserver

    def input(self, messageinput: GameMessages, data: Dict[str, any] = None) -> IClientState:
        pass

    def run(self):

        # visualizza il main menu
        self._viewcomposer.show(Templates.SECONDAITERAZIONE)

    def setPreviousState(self, state: IClientState):
        pass

    def giveData(self, data: Dict[str, any]):
        pass
