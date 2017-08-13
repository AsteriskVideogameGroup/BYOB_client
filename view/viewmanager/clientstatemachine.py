import os
from typing import Dict

import sys

from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.singleton import SingletonMetaclass
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.machinestates.iclientstate import IClientState


class ClientStateMachine(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._server: ServerWrapper = None
        self._viewcomposer: IViewComposer = None
        self._state: IClientState = None
        self._daofactory: IDAOAbstractFactory = None

    def init(self, initialstate: IClientState):
        # assegnazione dello stato iniziale alla macchina
        self._state = initialstate

        # inizializzazione dello stato
        self._state.initialize(self._server, self._viewcomposer, self._daofactory)

        # la macchina a stati si mette in ascolto dei messaggi da parte del server
        self._server.addListener(self._input)  # TODO deve essere decommentato

        # inizializzazione del view composer
        # la macchina a stati si mette in ascolto degli input utente
        self._viewcomposer.init(self._input)

        # run dello stato iniziale
        self._state.run()

        # avvio del viewcomposer
        self._viewcomposer.startWorking()

    def _input(self, message: GameMessages, data: Dict[str, any] = None):

        print("Messaggio ricevuto:")
        print(message)

        # controllo di uscita dal programma
        if message == GameMessages.EXITPROGRAM:
            os._exit(1)

        newstate: IClientState = self.currentstate.input(message, data)

        print(newstate)

        # lo stato potrebbe essere cambiato
        if newstate is not None:
            newstate.setPreviousState(self.currentstate)
            self.currentstate = newstate
            self.currentstate.initialize(self._server, self._viewcomposer, self._daofactory)
            self.currentstate.run()  # esecuzione del nuovo stato
        else:
            print("Nessun cambiamento di stato")

    @property
    def serverwrapper(self) -> ServerWrapper:
        return self._server

    @serverwrapper.setter
    def serverwrapper(self, wrapper: ServerWrapper):
        self._server = wrapper

    @property
    def viewcomposer(self) -> IViewComposer:
        return self._viewcomposer

    @viewcomposer.setter
    def viewcomposer(self, composer: IViewComposer):
        self._viewcomposer = composer

    @property
    def currentstate(self) -> IClientState:
        return self._state

    @currentstate.setter
    def currentstate(self, newstate: IClientState):
        self._state = newstate

    @property
    def daofactory(self) -> IDAOAbstractFactory:
        return self._daofactory

    @daofactory.setter
    def daofactory(self, f: IDAOAbstractFactory):
        self._daofactory = f


