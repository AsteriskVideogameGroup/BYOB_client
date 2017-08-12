from time import sleep

from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.inversionofcontrol.dicontainer import DepInjContainer
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


if __name__ == "__main__":

    # inizializzazione container IoC
    container: DepInjContainer = DepInjContainer().init("etc/config.json")

    # inizializzazione comunicazione di rete CORBA
    corbafactory: CorbaManagerFactory = container.getObject("corbamangerfactory")
    corbamanger: ICorbaManager = corbafactory.getCorbaManager()
    corbamanger.init()

    # instanziazione wrapper del server
    server: ServerWrapper = container.getObject("serverwrapper")
    server.init()

    # instanziazione wrapper del client e registrazione sul server
    client: Client = Client()
    client.playerid = "pepito.sbazzeguti@icloud.com"
    server.registerClient(client)

    # inizializzazione DAO
    corbafactory: IDAOAbstractFactory = container.getObject("daofactory")

    # inizializzazione macchina a stati
    machine: ClientStateMachine = container.getObject("clientstatemachine")
    initialstate: IClientState = MainMenuState()
    machine.init(initialstate)





