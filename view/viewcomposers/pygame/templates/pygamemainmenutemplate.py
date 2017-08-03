import os
from random import randint
from typing import Callable

import pygame

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameMainMenuTemplate(ITemplate):
    def __init__(self):
        self._eventlistnercallback: Callable[[object, GameMessages], None] = None
        self._screen = None

    def detachEventListerners(self, callback: Callable[[object, GameMessages], None]):
        pass

    def setAssets(self, **kwargs: dict):
        pass

    def print(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self._screen.fill((r, g, b))

    def getInputs(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print('Forward')
                self._eventlistnercallback(GameMessages.NEXT)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print('Backward')
                self._eventlistnercallback(GameMessages.PREVIOUS)

    def initialize(self, screen: object, observercallback: Callable[[object, GameMessages], None]) -> ITemplate:
        self._screen = screen
        self.registerEventListener(observercallback)

        return self

    def registerEventListener(self, callback: Callable[[object, GameMessages], None]):
        self._eventlistnercallback = callback
