from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.templates import Templates
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.machinestates.iclientstate import IClientState


class ExampleClientState(IClientState):

    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

    def run(self):
        print("sto runnando")

    def initialize(self, gameserver: ServerWrapper, viewcomposer: IViewComposer):
        print("inizializzato")
        self._viewcomposer = viewcomposer
        self._server = gameserver

    def update(self, messageinput: GameMessages) -> IClientState:
        print("updetato")

        self._viewcomposer.show(Templates.PROVA)  # TODO togliere

        return None
