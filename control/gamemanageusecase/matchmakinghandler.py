import Pyro4

from foundations.oophelpers.singleton import SingletonMetaclass

class MatchMakingHandler(metaclass=SingletonMetaclass):
    def makeNewGame(self, clientid: str, modeid: str, isranked: bool):
        pass
