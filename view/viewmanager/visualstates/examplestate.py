from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.viewsnames import ViewNames
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.visualstates.interfacevisualstate import IVisualState


class ExampleVisualState(IVisualState):

    def __init__(self):
        self._viewcomposer: IViewComposer = None
        self._server: ServerWrapper = None

    def run(self):
        print("sto runnando")

    def initialize(self, gameserver: ServerWrapper, viewcomposer: IViewComposer):
        print("inizializzato")
        self._viewcomposer = viewcomposer
        self._server = gameserver

    def update(self, messageinput: GameMessages) -> IVisualState:
        print("updetato")

        self._viewcomposer.show(ViewNames.PROVA)  # TODO togliere

        return None
