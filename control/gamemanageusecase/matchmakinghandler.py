import Pyro4

from foundations.oophelpers.singleton import SingletonMetaclass

@Pyro4.behavior(instance_mode="single")
@Pyro4.expose
class MatchMakingHandler(metaclass=SingletonMetaclass):
    def makeNewGame(self, clientid: str, modeid: str, isranked: bool):
        pass
