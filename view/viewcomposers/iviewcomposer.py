import abc
from typing import Callable

from view.viewcomposers.enumviews import EnumViews


class IViewComposer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self, eventlistener: Callable[[str], None]):
        pass

    @abc.abstractmethod
    def show(self, chosenview: EnumViews):
        pass
