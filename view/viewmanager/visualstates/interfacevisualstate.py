import abc

from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.state import State
from view.viewcomposers.iviewcomposer import IViewComposer


class IVisualState(State):

    @abc.abstractmethod
    def initialize(self, gameserver: ServerWrapper, viewmanager: IViewComposer):
        pass

