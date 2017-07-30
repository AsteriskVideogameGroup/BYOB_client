from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.singleton import SingletonMetaclass
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.visualstates.interfacevisualstate import IVisualState


class ViewManagerStateMachine(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._server: ServerWrapper = None
        self._viewcomposer: IViewComposer = None
        self._state: IVisualState = None

    @property
    def currentstate(self) -> IVisualState:
        return self._state

    @currentstate.setter
    def currentstate(self, newstate: IVisualState):
        self._state = newstate

    def initialize(self, server: ServerWrapper, viewcomposer: IViewComposer, initialstate: IVisualState):
        # assegnazione dello stato iniziale alla macchina
        self.currentstate = initialstate

        # inizializzazione dello stato
        self.currentstate.initialize(server, viewcomposer)

        # memorizzazione dei riferimenti agli oggetti server e viewcomposer
        # serviranno per i cambiamenti di stato
        self._server = server
        self._viewcomposer = viewcomposer

        # run dello stato iniziale
        self.currentstate.run()

    def input(self, message: GameMessages):
        newstate: IVisualState = self.currentstate.update(message)

        # lo stato potrebbe essere cambiato
        if newstate is not None:
            self.currentstate = newstate
            self.currentstate.initialize(self._server, self._viewcomposer)
        else:
            print("Nessun cambiamento di stato")

        # esecuzione dello stato
        self.currentstate.run()

