from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.visualstates.interfacevisualstate import IVisualState


class ExampleVisualState(IVisualState):
    def run(self):
        print("sto runnando")

    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        print("inizializzato")

    def update(self, input: GameMessages) -> IVisualState:
        return None
