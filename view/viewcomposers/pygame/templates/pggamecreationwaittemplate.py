from typing import Dict, Callable

import pygame

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameGameCreationWaitTemplate(ITemplate):
    def __init__(self):
        self._eventlistnercallback: Callable[[object, GameMessages, Dict[str, any]], None] = None
        self._screen = None

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def setAssets(self, kwargs: Dict[str, any]):
        pass

    def print(self):
        r = 0
        g = 255
        b = 0
        self._screen.fill((r, g, b))

    def getInputs(self):
        # TODO non fa niente
        for event in pygame.event.get():
            pass

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]) -> ITemplate:
        self._screen = screen.screen
        self.registerEventListener(observercallback)

        return self

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlistnercallback = callback
