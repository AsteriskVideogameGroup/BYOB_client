from typing import Callable, Dict

import pygame

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameUnrankedModeSelectionTemplate(ITemplate):
    def __init__(self):
        self._eventlistnercallback: Callable[[object, GameMessages, Dict[str, any]], None] = None
        self._screen = None

        # TODO togliere
        self._modeselected: str = "classic_mode"

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def setAssets(self, **kwargs: dict):
        pass

    def print(self):
        r = 255
        g = 0
        b = 0
        self._screen.fill((r, g, b))

    def getInputs(self):

        # TODO deve essere modificato
        for event in pygame.event.get():

            # System exit
            if event.type == pygame.QUIT:
                self._eventlistnercallback(GameMessages.EXITPROGRAM)

            # Key commands:
            # >, D: cursor to right (circularly)
            # <, A: cursor to left (circularly)
            # return, barspace: selection

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    # TODO modificare
                    self._eventlistnercallback(GameMessages.MODESELECTED, {"mode": self._modeselected})

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]) -> ITemplate:
        self._screen = screen.screen
        self.registerEventListener(observercallback)

        return self

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlistnercallback = callback
