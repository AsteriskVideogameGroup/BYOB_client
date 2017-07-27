import abc

from view.viewcomposers.enumviews import EnumViews


class IViewComposer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, eventhandlercallback: callable):
        pass

    @abc.abstractmethod
    def show(self, chosenview: EnumViews):
        pass
