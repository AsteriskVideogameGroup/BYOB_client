import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.sysmessages.gamemessages import GameMessages
from foundations.joypadsupport.joypadcontrol import JoypadControl
from view.viewcomposers.itemplate import ITemplate


class PyGameMainMenuTemplate(ITemplate):  # TODO mettere ereditarietà dal template

    _MENUELEMENTSIZE = (220, 300)
    _CHARACTERSIZE = (600, 600)
    _EXITSIZE = (100, 100)
    _ARROWSIZE = (100, 100)
    _SCREENSIZE = (1280, 720)  # TODO METTERE IN FILE DI CONFIGURAZIONE
    _TITLESIZE = (1000, 100)
    _EXITARROWSIZE = (50, 50)

    _PATH: str = "foundations/media/mainmenu/"

    def __init__(self):
        self._menuelement = list()
        self._eventlistnercallback = None
        self._screen = None

        #dir = os.path.dirname(__file__)
        #self._assetspath: str = os.path.join(dir, '../../../foundations/media/mainmenu/')

        #print(self._assetspath)


        self._background = None
        self._exit = None
        self._character = None
        self._title = None
        self._genericelement = None
        self._elemarrow = None
        self._rotatedarrow = None
        self._selected = None

    def initialize(self, screen: object, observercallback: Callable[[object, GameMessages], None]):

        self._screen = screen
        self.registerEventListener(observercallback)

        self._background = pygame.image.load(PyGameMainMenuTemplate._PATH + 'background.png')
        self._background = pygame.transform.scale(self._background, PyGameMainMenuTemplate._SCREENSIZE)

        self._exit = pygame.image.load(PyGameMainMenuTemplate._PATH + 'exit.png')
        self._exit = pygame.transform.scale(self._exit, PyGameMainMenuTemplate._EXITSIZE)

        self._character = pygame.image.load(PyGameMainMenuTemplate._PATH + 'character.png')
        self._character = pygame.transform.scale(self._character, PyGameMainMenuTemplate._CHARACTERSIZE)

        self._title = pygame.image.load(PyGameMainMenuTemplate._PATH + 'title.png')
        self._title = pygame.transform.scale(self._title, PyGameMainMenuTemplate._TITLESIZE)

        self._genericelement = pygame.image.load(PyGameMainMenuTemplate._PATH + 'menuelement.png')
        self._genericelement = pygame.transform.scale(self._genericelement, PyGameMainMenuTemplate._MENUELEMENTSIZE)

        elem1 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'quickmatch.png')
        elem2 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'rankedmatch.png')
        elem3 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'comingsoon.png')

        self._menuelement.append(pygame.transform.scale(elem1, PyGameMainMenuTemplate._MENUELEMENTSIZE))
        self._menuelement.append(pygame.transform.scale(elem2, PyGameMainMenuTemplate._MENUELEMENTSIZE))
        self._menuelement.append(pygame.transform.scale(elem3, PyGameMainMenuTemplate._MENUELEMENTSIZE))

        self._elemarrow = pygame.image.load(PyGameMainMenuTemplate._PATH + 'arrow.png')
        self._elemarrow = pygame.transform.scale(self._elemarrow, PyGameMainMenuTemplate._ARROWSIZE)

        self._rotatedarrow = pygame.transform.rotate(self._elemarrow, 270)
        self._rotatedarrow = pygame.transform.scale(self._rotatedarrow, PyGameMainMenuTemplate._EXITARROWSIZE)

        self._selected = 0

    def print(self):

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)
        self._screen.blit(self._title, zeropos)

        characterposition = (900, 130)
        self._screen.blit(self._character, characterposition)

        i = 0
        step = 50
        elementstartingposition = (70, 240)

        for element in self._menuelement:
            self._screen.blit(self._genericelement, (
                elementstartingposition[0] + i * (self._MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            self._screen.blit(element, (
                elementstartingposition[0] + i * (self._MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            i = i + 1

        exitposition = (1150, 0)
        self._screen.blit(self._exit, exitposition)

        arrowstartposition = (130, 560)
        if self._selected < 3:
            self._screen.blit(self._elemarrow, (
                arrowstartposition[0] + self._selected * (self._MENUELEMENTSIZE[0] + step), arrowstartposition[1]))
        else:
            self._screen.blit(self._rotatedarrow, (1110, 30))

    def getInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._eventlistnercallback(GameMessages.EXITPROGRAM)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self._select(-1)
                elif event.key == pygame.K_d:
                    self._select(1)
                elif event.key == pygame.K_RETURN:
                    self._enter()

            elif event.type == pygame.JOYAXISMOTION:
                threshold = 0.95
                if event.axis == JoypadControl.AXIS0:  # "AXIS 0" E' L'ANALOGICO IN ALTO A SINISTRA DI UN JOYPAD XBOX360
                    if event.value > threshold:
                        self._select(1)
                    elif event.value < -threshold:
                        self._select(-1)

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == JoypadControl.BUTTON0:  # BOTTONE A DI UN JOYPAD XBOX360
                    self._enter()

            elif event.type == pygame.JOYHATMOTION:
                if event.hat == JoypadControl.DPAD:
                    self._select(event.value[0])

    def _enter(self):
        if self._selected == 3:
            self._eventlistnercallback(GameMessages.EXITPROGRAM)
        elif self._selected == 0:
            self._eventlistnercallback(GameMessages.INITUNRANKEDGAME)

    def _select(self, direction: int):
        self._selected = (self._selected + direction) % 4

    def setAssets(self, **kwargs: dict):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages], None]):
        self._eventlistnercallback = callback
