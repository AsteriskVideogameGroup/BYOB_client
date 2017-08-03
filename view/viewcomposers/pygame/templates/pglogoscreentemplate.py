from typing import Callable

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameLogoScreenTemplate(ITemplate):

    def __init__(self):
        self._eventlistnercallback: Callable[[object, GameMessages], None] = None
        self._screen = None

    def setAssets(self, **kwargs: dict):
        pass

    def initialize(self, screen: object, observercallback: Callable[[object, GameMessages], None]) -> ITemplate:
        self._screen = screen
        self.registerEventListener(observercallback)

        return self

    def registerEventListener(self, callback: Callable[[object, GameMessages], None]):
        self._eventlistnercallback = callback

    def print(self):
        pass

    def getInputs(self):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages], None]):
        pass