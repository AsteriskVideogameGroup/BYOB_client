import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate
from foundations.screenutils.screen import Screen


class PyGameGameWaitingTemplate(ITemplate):
    _CHARACTERSIZE = (100, 100)
    _LOOPSECONDS = 4

    _MEDIAPATH = "waiting/"
    _FONTPATH = "font/"

    def __init__(self):

        self._eventlistnercallback = None
        self._screen = None
        self._screendims = None
        self._background = None
        self._callnumber = 0
        self._loopduration = 0
        self._fps = 0
        self._character = []

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]):

        # Color initialization

        WHITE = (255, 255, 255)

        # Font init

        pygame.font.init()
        font_path = mediapath + PyGameGameWaitingTemplate._FONTPATH + "Emulogic/emulogic.ttf"
        font_size = 24
        self._font = pygame.font.Font(font_path, font_size)

        # Mediapath init

        self._mediapath = mediapath + PyGameGameWaitingTemplate._MEDIAPATH

        # Screen initialization

        self._screen = screen.screen
        self._fps = screen.fps
        self._screendims = screen.dimensions

        # Animation duration

        self._loopduration = screen.fps * 4

        # Callback init

        self.registerEventListener(observercallback)

        # Background loading and resizing

        self._background = pygame.image.load(self._mediapath + 'background.png')
        self._background = pygame.transform.scale(self._background, self._screendims)

        # Character loading and resizing

        self._character = [
            pygame.transform.scale(pygame.image.load(self._mediapath + 'characterfl.png'),
                                   PyGameGameWaitingTemplate._CHARACTERSIZE),
            pygame.transform.scale(pygame.image.load(self._mediapath + 'characterfr.png'),
                                   PyGameGameWaitingTemplate._CHARACTERSIZE),
        ]

    def print(self):

        # Background positioning and print

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)

        # Color definition

        WHITE = (255, 255, 255)
        YELLOW = (255, 240, 1)

        # Loading string rendering, positioning and print

        loadingstring = "Looking for a game" + "." * int(
            (1 * self._callnumber / self._fps) % PyGameGameWaitingTemplate._LOOPSECONDS)
        loadinglabel = self._font.render(loadingstring, 1, WHITE)
        labeldimensions = (loadinglabel.get_rect().width, loadinglabel.get_rect().height)

        loadingposition = ((self._screendims[0] - labeldimensions[0]) / 2,
                           (self._screendims[1] - labeldimensions[1]) / 2 + 2 * labeldimensions[1])
        self._screen.blit(loadinglabel, loadingposition)

        # Character selecting, positioning and print

        characterposition = ((self._screendims[0] - PyGameGameWaitingTemplate._CHARACTERSIZE[0]) / 2,
                             (self._screendims[1] - PyGameGameWaitingTemplate._CHARACTERSIZE[1]) / 2 - labeldimensions[1])
        characternum = int(self._callnumber > self._loopduration / 2)
        self._screen.blit(self._character[characternum], characterposition)

        # Question marks rendering, positioning and print

        questionmark = self._font.render("?", 1, YELLOW)
        questionmarkdimensions = (questionmark.get_rect().width, questionmark.get_rect().height)
        questionmarkpositions = [
            (characterposition[0] + PyGameGameWaitingTemplate._CHARACTERSIZE[0],
             characterposition[1]),
            (characterposition[0] + PyGameGameWaitingTemplate._CHARACTERSIZE[0] + questionmarkdimensions[0],
             characterposition[1] - questionmarkdimensions[1]),
            (characterposition[0] + PyGameGameWaitingTemplate._CHARACTERSIZE[0],
             characterposition[1] - 2 * questionmarkdimensions[1]),
        ]
        for i in range(int((1 * self._callnumber / self._fps) % PyGameGameWaitingTemplate._LOOPSECONDS)):
            self._screen.blit(questionmark, questionmarkpositions[i])

        # Increasing of number of print() made on this screen

        self._callnumber = (self._callnumber + 1) % self._loopduration

    def getInputs(self):
        for event in pygame.event.get():
            # System exit
            if event.type == pygame.QUIT:
                self._eventlistnercallback(GameMessages.EXITPROGRAM)

    def setAssets(self, kwargs: Dict[str, any]):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlistnercallback = callback
