import abc
from typing import Dict

from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.state import State
from view.viewcomposers.iviewcomposer import IViewComposer


class IClientState(State):

    @abc.abstractmethod
    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer, daofactory: IDAOAbstractFactory):
        pass

    @abc.abstractmethod
    def giveData(self, data: Dict[str, any]):
        pass

    @abc.abstractmethod
    def setPreviousState(self, state: State):
        pass

