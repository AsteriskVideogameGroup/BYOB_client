from threading import Thread

import Pyro4

from foundations.network.corba.icorbamanager import ICorbaManager


class PyroCorbaManager(ICorbaManager):
    def __init__(self):
        self._nsaddress: str = None
        self._nsport: int = None
        self._daemon: Pyro4.Daemon = None
        self._ns = None

    def init(self, nsaddress: str = "localhost", nsport: int = 9090):

        self._nsaddress = nsaddress
        self._nsport = nsport
        self._daemon = Pyro4.Daemon()

        self._ns = Pyro4.locateNS(nsaddress, nsport)

        # start del demone pyro
        Thread(target=self._daemon.requestLoop, args=()).start()

    def getFromSystem(self, objectid: str):
        return Pyro4.Proxy("PYRONAME:{0}".format(objectid))

    def remotize(self, obj: object, objname: str = None) -> str:

        # if objname is None:
        uri = self._daemon.register(obj)

        if objname is None:
            objname = str(uri.object)

        self._ns.register(objname, uri)

        return objname