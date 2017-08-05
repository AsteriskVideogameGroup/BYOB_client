import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from foundations.joypadsupport.joypadcontrol import JoypadControl
from view.viewcomposers.itemplate import ITemplate


class PyGameMainMenuTemplate(ITemplate):  # TODO mettere ereditarietà dal template

    # Template menu dimensions
    _MENUELEMENTSIZE = (220, 300)
    _CHARACTERSIZE = (600, 600)
    _EXITSIZE = (100, 100)
    _ARROWSIZE = (100, 100)
    _TITLESIZE = (1000, 100)
    _EXITARROWSIZE = (50, 50)

    # Number of selectable elements
    _SELECTABLEITEMS = 4

    # nome della cartella dei media
    _MEDIAFOLDER: str = "mainmenu/"

    def __init__(self):
        self._menuelement = list()
        self._eventlistnercallback = None
        self._screen = None
        self._mediapath: str = None

        self._background = None
        self._exit = None
        self._character = None
        self._title = None
        self._genericelement = None
        self._elemarrow = None
        self._rotatedarrow = None
        self._selected = 0

    def initialize(self, screen: Screen, mediapath: str, observercallback: Callable[[object, GameMessages], None]):

        self._screen: pygame.Surface = screen.screen
        self.registerEventListener(observercallback)
        self._mediapath = mediapath + PyGameMainMenuTemplate._MEDIAFOLDER

        # Background loading and resizing

        self._background = pygame.image.load(self._mediapath + 'background.png')
        self._background = pygame.transform.scale(self._background, screen.dimensions)

        # Exit icon loading and resizing

        self._exit = pygame.image.load(self._mediapath + 'exit.png')
        self._exit = pygame.transform.scale(self._exit, PyGameMainMenuTemplate._EXITSIZE)

        # Menu character image loading and resizing

        self._character = pygame.image.load(self._mediapath + 'character.png')
        self._character = pygame.transform.scale(self._character, PyGameMainMenuTemplate._CHARACTERSIZE)

        # Title icon loading and resizing

        self._title = pygame.image.load(self._mediapath + 'title.png')
        self._title = pygame.transform.scale(self._title, PyGameMainMenuTemplate._TITLESIZE)

        # Generic menu element skeleton loading and resizing

        self._genericelement = pygame.image.load(self._mediapath + 'menuelement.png')
        self._genericelement = pygame.transform.scale(self._genericelement, PyGameMainMenuTemplate._MENUELEMENTSIZE)

        # Specific menu element loading and resizing

        elem1 = pygame.image.load(self._mediapath + 'quickmatch.png')
        elem2 = pygame.image.load(self._mediapath + 'rankedmatch.png')
        elem3 = pygame.image.load(self._mediapath + 'comingsoon.png')
        self._menuelement.append(pygame.transform.scale(elem1, PyGameMainMenuTemplate._MENUELEMENTSIZE))
        self._menuelement.append(pygame.transform.scale(elem2, PyGameMainMenuTemplate._MENUELEMENTSIZE))
        self._menuelement.append(pygame.transform.scale(elem3, PyGameMainMenuTemplate._MENUELEMENTSIZE))

        # Menu cursor icon loading and resizing

        self._elemarrow = pygame.image.load(self._mediapath + 'arrow.png')
        self._elemarrow = pygame.transform.scale(self._elemarrow, PyGameMainMenuTemplate._ARROWSIZE)

        # Definition of the exit arrow (rotation of the cursor and resizing)

        self._rotatedarrow = pygame.transform.rotate(self._elemarrow, 270)
        self._rotatedarrow = pygame.transform.scale(self._rotatedarrow, PyGameMainMenuTemplate._EXITARROWSIZE)

    def print(self):

        # Background and title positioning and print

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)
        self._screen.blit(self._title, zeropos)

        # Character positioning and print

        characterposition = (900, 130)
        self._screen.blit(self._character, characterposition)

        # Menu elements positioning and print

        i = 0
        step = 50
        elementstartingposition = (70, 240)

        for element in self._menuelement:
            self._screen.blit(self._genericelement, (
                elementstartingposition[0] + i * (self._MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            self._screen.blit(element, (
                elementstartingposition[0] + i * (self._MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            i = i + 1

        # Exit positioning and print

        exitposition = (1150, 0)
        self._screen.blit(self._exit, exitposition)

        # Cursor positioning and print

        arrowstartposition = (130, 560)
        if self._selected < 3:
            # Cursor on menu elements
            self._screen.blit(self._elemarrow, (
                arrowstartposition[0] + self._selected * (self._MENUELEMENTSIZE[0] + step), arrowstartposition[1]))
        else:
            # Cursor on exit icon
            self._screen.blit(self._rotatedarrow, (1110, 30))

    def getInputs(self):

        # Threshold for the axis detection

        axisthreshold = 0.99

        for event in pygame.event.get():

            # System exit
            if event.type == pygame.QUIT:
                self._eventlistnercallback(GameMessages.EXITPROGRAM)

            # Key commands:
            # >, D: cursor to right (circularly)
            # <, A: cursor to left (circularly)
            # return, barspace: selection

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self._select(-1)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self._select(1)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self._enter()

            # Joypad commands:
            # AXIS0 to right, DPAD right: cursor to right (circularly)
            # AXIS0 to left, DPAD left: cursor to left (circularly)
            # Button0: selection

            elif event.type == pygame.JOYAXISMOTION:
                value = event.value
                if abs(value) > axisthreshold:

                    if event.axis == JoypadControl.AXIS0:

                        if value > 0:
                            self._select(1)
                        else:
                            self._select(-1)

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == JoypadControl.BUTTON0:
                    self._enter()

            elif event.type == pygame.JOYHATMOTION:
                if event.hat == JoypadControl.DPAD:
                    self._select(event.value[0])

    def _enter(self):
        # If is selected the exit icon

        if self._selected == 3:
            self._eventlistnercallback(GameMessages.EXITPROGRAM)

        # If is selected the first menu element

        elif self._selected == 0:
            self._eventlistnercallback(GameMessages.INITUNRANKEDGAME)

    def _select(self, direction: int):

        # Move the cursor of 'direction' positions to right (can be negative) circularly

        self._selected = (self._selected + direction) % PyGameMainMenuTemplate._SELECTABLEITEMS

    def setAssets(self, **kwargs: dict):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages], None]):
        self._eventlistnercallback = callback
