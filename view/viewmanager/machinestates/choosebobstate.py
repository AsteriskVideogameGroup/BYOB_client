from typing import Dict, List

from foundations.dao.iclientbobdao import IClientBobDAO
from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.state import State
from foundations.sysmessages.gamemessages import GameMessages
from model.gamemanage.clientbobdescription import ClientBobDescription
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.templates import Templates
from view.viewmanager.machinestates.iclientstate import IClientState

#TODO DA RIMUOVERE
from view.viewmanager.machinestates.tempsecondaiterazionestate import *


class ChooseBobState(IClientState):
    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None
        self._data: Dict[str, any] = None
        self._daofactory: IDAOAbstractFactory = None

    def run(self):
        self._viewcomposer.show(Templates.CHOOSEBOB)

        bobs: List[ClientBobDescription] = self._daofactory.getClientBobDAO().getAll()

        self._viewcomposer.setAssets({"bobs": bobs})

    def setPreviousState(self, state: State):
        pass

    def giveData(self, data: Dict[str, any]):
        pass

    def input(self, messageinput: GameMessages, data: Dict[str, any] = None) -> IClientState:
        newstate: IClientState = None

        if messageinput == GameMessages.BOBCHOSEN:

            # comunica al server la scelta
            self._server.chooseBob(data["bob_id"])

        if messageinput == GameMessages.MAPREADY:
            # TODO DA MODIFICARE
            newstate = TempSecondaIterazioneState()

        return newstate

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, daofactory: IDAOAbstractFactory):
        self._viewcomposer = viewmanager
        self._server = gameserver
        self._daofactory = daofactory
