from time import sleep

from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.pygame.pygamecomposer import PyGameComposer
from view.viewmanager.clientstatemachine import ClientStateMachine
from view.viewmanager.machinestates.iclientstate import IClientState
from view.viewmanager.machinestates.mainmenustate import MainMenuState

corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
corba.init()

client: Client = Client()

server: ServerWrapper = ServerWrapper()

server.init(corba)
server.registerClient(client)

print("tutto ok fin qui")


machine: ClientStateMachine = ClientStateMachine()
viewcomposer: IViewComposer = PyGameComposer()
initialstate: IClientState = MainMenuState()

machine.initialize(server, viewcomposer, initialstate)

print("pure qui ok")

#machine.input(GameMessages.INITUNRANKEDGAME)

print("pure qui ok 2")


