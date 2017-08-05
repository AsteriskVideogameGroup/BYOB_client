from typing import Callable

import pygame

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameGameSelectionTemplate(ITemplate):

    def __init__(self):
        self._eventlistnercallback: Callable[[object, GameMessages], None] = None
        self._screen = None

    def detachEventListerners(self, callback: Callable[[object, GameMessages], None]):
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print('Forward')
                self._eventlistnercallback(GameMessages.NEXT)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print('Backward')
                self._eventlistnercallback(GameMessages.PREVIOUS)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('Selected')
                self._eventlistnercallback(GameMessages.ACCEPT)

    def initialize(self, screen: Screen, mediapath: str, observercallback: Callable[[object, GameMessages], None]) -> ITemplate:
        self._screen = screen.screen
        self.registerEventListener(observercallback)

        return self

    def registerEventListener(self, callback: Callable[[object, GameMessages], None]):
        self._eventlistnercallback = callback