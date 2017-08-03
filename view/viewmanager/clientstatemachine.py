from typing import Dict

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

    @property
    def currentstate(self) -> IClientState:
        return self._state

    @currentstate.setter
    def currentstate(self, newstate: IClientState):
        self._state = newstate

    def initialize(self, server: ServerWrapper, viewcomposer: IViewComposer, initialstate: IClientState):
        # assegnazione dello stato iniziale alla macchina
        self.currentstate = initialstate

        # inizializzazione dello stato
        self.currentstate.initialize(server, viewcomposer)

        # memorizzazione dei riferimenti agli oggetti server e viewcomposer
        # serviranno per i cambiamenti di stato
        self._server = server
        self._viewcomposer = viewcomposer

        # la macchina a stati si mette in ascolto dei messaggi da parte del server
        # self._server.addListener(self.input) # TODO deve essere decommentato

        # inizializzazione del view composer
        # la macchina a stati si mette in ascolto degli input utente
        self._viewcomposer.init(self.input)

        # run dello stato iniziale
        self.currentstate.run()

        # avvio del viewcomposer
        self._viewcomposer.startWorking()

    def input(self, message: GameMessages):
        newstate: IClientState = self.currentstate.input(message)

        # lo stato potrebbe essere cambiato
        if newstate is not None:
            self.currentstate = newstate
            self.currentstate.initialize(self._server, self._viewcomposer)
            self.currentstate.run()  # esecuzione del nuovo stato
        else:
            print("Nessun cambiamento di stato")


