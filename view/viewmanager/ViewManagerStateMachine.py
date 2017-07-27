from foundations.network.serverwrapper.serverwrapper import ServerWrapper
from foundations.oophelpers.singleton import SingletonMetaclass
from view.viewcomposers.iviewcomposer import IViewComposer
from view.viewmanager.visualstates.interfacevisualstate import IVisualState


class ViewManagerStateMachine(metaclass=SingletonMetaclass):
    """"""

    def __init__(self, server: ServerWrapper, viewcomposer: IViewComposer, initialstate: IVisualState):
        self._server: ServerWrapper = server
        pass
