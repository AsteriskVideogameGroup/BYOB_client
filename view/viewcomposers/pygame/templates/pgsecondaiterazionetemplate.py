import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from foundations.joypadsupport.joypadcontrol import JoypadControl
from view.viewcomposers.itemplate import ITemplate


class PyGameSecondaIterazioneTemplate(ITemplate):


    # nome della cartella dei media
    _MEDIAFOLDER: str = "mainmenu/"
    _FONTPATH = "font/"

    def __init__(self):
        self._menuelement = list()
        self._eventlistnercallback = None
        self._screen = None
        self._mediapath: str = None

        self._background = None


        self._isalreadyinitialized: bool = False  # true se è già stato inizializzato

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]):

        font_path = mediapath + PyGameSecondaIterazioneTemplate._FONTPATH + "Emulogic/emulogic.ttf"
        font_name_size = 24
        self._font_title = pygame.font.Font(font_path, font_name_size)
        WHITE = (255, 255, 255)

        self._message = self._font_title.render("Coming soon... nella seconda iterazione", 1, WHITE)

        if self._isalreadyinitialized is False:
            self._screen: pygame.Surface = screen.screen
            self.registerEventListener(observercallback)
            self._mediapath = mediapath + PyGameSecondaIterazioneTemplate._MEDIAFOLDER

            # Background loading and resizing

            self._background = pygame.image.load(self._mediapath + 'background.png')
            self._background = pygame.transform.scale(self._background, screen.dimensions)


            self._isalreadyinitialized = True

        self._screen = screen.screen
        self._screendims = screen.dimensions

    def print(self):

        # Background and title positioning and print

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)


        messageposition = ((self._screendims[0] - self._message.get_rect().width) / 2,
                         self._screendims[1] / 4)
        self._screen.blit(self._message, messageposition)


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
