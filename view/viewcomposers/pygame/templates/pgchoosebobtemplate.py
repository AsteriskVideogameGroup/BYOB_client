from typing import Callable, Dict

import pygame

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameChooseBobTemplate(ITemplate):
    def __init__(self):
        self._screen: Screen = None
        self._eventlistnercallback: Callable[[object, GameMessages, Dict[str, any]], None] = None

    def print(self):
        self._screen.screen.fill((0, 0, 255))

    def getInputs(self):
        for event in pygame.event.get():
            # System exit
            if event.type == pygame.QUIT:
                self._eventlistnercallback(GameMessages.EXITPROGRAM)

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def setAssets(self, kwargs: Dict[str, any]):
        pass

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]) -> ITemplate:
        self._screen = screen
        self._eventlistnercallback = observercallback
        return self
