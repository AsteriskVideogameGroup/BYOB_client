from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.inversionofcontrol.iioccontainer import IIoCContainer
from foundations.inversionofcontrol.ioccontainer import InversionOfControlContainer
from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from view.viewmanager.clientstatemachine import ClientStateMachine
from view.viewmanager.machinestates.iclientstate import IClientState
from view.viewmanager.machinestates.mainmenustate import MainMenuState


if __name__ == "__main__":

    # inizializzazione container IoC
    container: IIoCContainer = InversionOfControlContainer().init("etc/config.json")

    # inizializzazione comunicazione di rete CORBA
    corbafactory: CorbaManagerFactory = container.getObject("corbamangerfactory")
    corbamanger: ICorbaManager = corbafactory.getCorbaManager()
    corbamanger.init()

    # instanziazione wrapper del server
    server: ServerWrapper = container.getObject("serverwrapper")
    server.init()

    # instanziazione wrapper del client e registrazione sul server
    client: Client = Client()
    client.playerid = "p3"
    server.registerClient(client)

    # inizializzazione DAO
    daofactory: IDAOAbstractFactory = container.getObject("daofactory")
    daofactory.init()

    # inizializzazione macchina a stati
    machine: ClientStateMachine = container.getObject("clientstatemachine")
    initialstate: IClientState = MainMenuState()
    machine.init(initialstate)





