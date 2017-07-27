from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.serverwrapper.serverwrapper import ServerWrapper


corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
corba.init()

client: Client = Client("user1")

server: ServerWrapper = ServerWrapper()

server.init(corba)

print("tutto ok fin qui")


