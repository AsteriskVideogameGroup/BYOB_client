from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewcomposers.pygame.pygamecomposer import PyGameComposer
from view.viewmanager.ViewManagerStateMachine import ViewManagerStateMachine
from view.viewmanager.visualstates.examplestate import ExampleVisualState
from view.viewmanager.visualstates.interfacevisualstate import IVisualState

corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
corba.init()

client: Client = Client("user1")

server: ServerWrapper = ServerWrapper()

server.init(corba)
server.register(client)

print("tutto ok fin qui")


manager: ViewManagerStateMachine = ViewManagerStateMachine()
viewcomposer: IViewComposer = PyGameComposer()
initialstate: IVisualState = ExampleVisualState()


manager.initialize(server, viewcomposer, initialstate)
print("pure qui ok")

manager.input(GameMessages.GAMECREATED)




