import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from foundations.joypadsupport.joypadcontrol import JoypadControl
from view.viewcomposers.itemplate import ITemplate
from model.clientgamemanage.clientbob import ClientBob


class PyGameBobSelectionTemplate():#ITemplate):

    _CURSORSIZE = (100, 100)
    _NAMEFRAMESIZE = (700, 100)
    _ICONSIZE = (30,30)
    _DESCRIPTIONSIZE = (380, 550)
    _BUTTONSSIZE = (200, 50)
    _CHARACTERSOFSET = 20
    _CHARACTERSIZE = (66, 66)
    _PORTRAITDIMENSIONS = (150,150)
    _COUNTDOWNSTART = 10 # TODO DA FILE
    _BOBSCOLUMN = 5
    _MEDIAPATH = "bobselection/"
    _FONTPATH = "font/"

    def __init__(self):

        self._fontpath = None
        self._mediapath = None
        self._eventlistenercallback = None
        self._screen = None
        self._screendims = None
        self._modelbobs = []
        self._matrixbobs = []
        self._background = None
        self._title = None
        self._descriptionframe = None
        self._cursor = None
        self._icons = {}
        for i in range(PyGameBobSelectionTemplate._BOBSCOLUMN):
            self._modelbobs.append([])
            self._matrixbobs.append([])
        self._selected = (1, 0)
        self._canchoose = False
        self._currentcall = 0
        self._fps = 0

    def initialize(self, screen: Screen, mediapath: str,
                   observercallback: Callable[[object, GameMessages, Dict[str, any]], None]):
        WHITE = (255, 255, 255)
        YELLOW = (255, 240, 1)

        # Font init

        pygame.font.init()
        self._fontpath = mediapath + PyGameBobSelectionTemplate._FONTPATH + "Emulogic/emulogic.ttf"
        self._mediapath = mediapath + PyGameBobSelectionTemplate._MEDIAPATH

        # Screen details init

        self._screen = screen.screen
        self._screendims = screen.dimensions
        self._fps = screen.fps


        # Callback init

        self.registerEventListener(observercallback)

        # Background loading and resizing

        self._background = pygame.image.load(self._mediapath + 'background.png')
        self._background = pygame.transform.scale(self._background, self._screendims)

        # Title defining
        self._title = "Choose your BoB!"

        # Description frame picture loading and resizing

        self._descriptionframe = pygame.image.load(self._mediapath + 'descriptionframe.png')
        self._descriptionframe = pygame.transform.scale(self._descriptionframe,
                                                        PyGameBobSelectionTemplate._DESCRIPTIONSIZE)

        # Menu cursor icon loading and resizing

        self._cursor = pygame.image.load(self._mediapath + 'cursor.png')
        self._cursor = pygame.transform.scale(self._cursor, PyGameBobSelectionTemplate._CURSORSIZE)

        # Menu icon loading and resizing

        self._icons = {
            'damage': pygame.transform.scale(pygame.image.load(self._mediapath + 'icons/damage.png'),
                                             PyGameBobSelectionTemplate._ICONSIZE),
            'life': pygame.transform.scale(pygame.image.load(self._mediapath + 'icons/life.png'),
                                           PyGameBobSelectionTemplate._ICONSIZE),
            'range': pygame.transform.scale(pygame.image.load(self._mediapath + 'icons/range.png'),
                                            PyGameBobSelectionTemplate._ICONSIZE),
            'bombnumber': pygame.transform.scale(pygame.image.load(self._mediapath + 'icons/bombnumber.png'),
                                                 PyGameBobSelectionTemplate._ICONSIZE),
            'speed': pygame.transform.scale(pygame.image.load(self._mediapath + 'icons/speed.png'),
                                            PyGameBobSelectionTemplate._ICONSIZE),
            'power': pygame.font.Font(self._fontpath, 24).render("S", 1, YELLOW)
        }

        # From now to the end of countdown the user can choose the Bob

        self._canchoose = True
        
    def print(self):

        WHITE = (255,255,255)

        # Background print

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)

        # Title positioning and print

        title = ""
        font_title_size = 24
        if self._canchoose:
            remainingtime = PyGameBobSelectionTemplate._COUNTDOWNSTART - int(self._currentcall/self._fps)
            if remainingtime > 0:
                title = self._title + ' - ' + str(remainingtime)
            else:
                self._canchoose = False
        else:
            title = self._title + " - Waiting for your opponents"

        font_title = pygame.font.Font(self._fontpath, font_title_size)
        printabletitle = font_title.render(title, 1, WHITE)
        titleposition = ((self._screendims[0] - printabletitle.get_rect().width) / 2,
                         self._screendims[1] / 20)
        self._screen.blit(printabletitle, titleposition)

        # Bob selectable positioning and print

        bobdistance = 50
        positions = {}
        position = (self._screendims[0] / 9, self._screendims[1] / 5.5)

        for i in range(len(self._matrixbobs)):
            for j in range(len(self._matrixbobs[i])):
                positions[(i,j)] = position
                bob = pygame.transform.scale(self._matrixbobs[i][j], PyGameBobSelectionTemplate._CHARACTERSIZE)
                self._screen.blit(bob, position)
                position = (position[0], position[1] + bobdistance + PyGameBobSelectionTemplate._CHARACTERSIZE[1])
            position = (
            position[0] + bobdistance + PyGameBobSelectionTemplate._CHARACTERSIZE[0], self._screendims[1] / 5.5)

        # Cursor positioning and print

        cursorposition = (positions[self._selected][0] - PyGameBobSelectionTemplate._CURSORSIZE[0]/5,
                          positions[self._selected][1] - PyGameBobSelectionTemplate._CURSORSIZE[1]/9)
        if self._canchoose:
            self._screen.blit(self._cursor, cursorposition)

        # Description frame positioning and print

        descriptionframeposition = (self._screendims[0]*(8.3/9) - PyGameBobSelectionTemplate._DESCRIPTIONSIZE[0],
                                    self._screendims[1] / 6.5)
        self._screen.blit(self._descriptionframe, descriptionframeposition)

        # Selected bob portrait positioning and print

        portraitposition = (descriptionframeposition[0] + PyGameBobSelectionTemplate._DESCRIPTIONSIZE[0]/3.2,
                            descriptionframeposition[1] + PyGameBobSelectionTemplate._DESCRIPTIONSIZE[1]/11)
        portrait = pygame.transform.scale(self._matrixbobs[self._selected[0]][self._selected[1]], PyGameBobSelectionTemplate._PORTRAITDIMENSIONS)
        self._screen.blit(portrait, portraitposition)

        # Selected bob name positioning and print

        currentbob =  self._modelbobs[self._selected[0]][self._selected[1]]
        bobname = currentbob.name
        font_name_size = 20
        fontname = pygame.font.Font(self._fontpath, font_name_size)
        bobname = fontname.render(bobname,1,WHITE)
        textwidth = bobname.get_rect().width
        bobnameposition = (descriptionframeposition[0] + (PyGameBobSelectionTemplate._DESCRIPTIONSIZE[0]-textwidth)/2,
                           descriptionframeposition[1] + PyGameBobSelectionTemplate._DESCRIPTIONSIZE[1]*(.4))
        self._screen.blit(bobname, bobnameposition)

        # Selected bob (and icons) stats positioning and print

        iconstep = 5
        iconposition = (descriptionframeposition[0] + PyGameBobSelectionTemplate._DESCRIPTIONSIZE[0] * (1/10),
                    bobnameposition[1] + PyGameBobSelectionTemplate._DESCRIPTIONSIZE[0] * (1/4))
        statsfontsize = 20
        stats = {
            'life' : str(currentbob.lifemodifier),
            'damage': str(currentbob.damagemodifier),
            'range': str(currentbob.rangemodifier),
            'power': str(currentbob.power),
            'bombnumber': str(currentbob.placeblebombsmodifier),
            'speed': str(currentbob.speedmodifier)
        }
        for key in self._icons.keys():
            self._screen.blit(self._icons[key],iconposition)
            stat = pygame.font.Font(self._fontpath, statsfontsize).render(": " + stats[key], 1, WHITE)
            statposition = (iconposition[0] + PyGameBobSelectionTemplate._ICONSIZE[0],
                            iconposition[1])
            self._screen.blit(stat, statposition)

            iconposition = (iconposition[0],
                        iconposition[1] + PyGameBobSelectionTemplate._ICONSIZE[0] + iconstep)


        self._currentcall = (self._currentcall + 1)% (PyGameBobSelectionTemplate._COUNTDOWNSTART*self._fps + 1)

    def getInputs(self):
        for event in pygame.event.get():

            # System exit
            if event.type == pygame.QUIT:
                self._eventlistenercallback(GameMessages.EXITPROGRAM)
                pass

            # Navigation input from keyboard

            if self._canchoose:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self._horizzontalnavigation(-1)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self._verticalnavigation(-1)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self._horizzontalnavigation(1)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self._verticalnavigation(1)

                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self._enter()

                # Navigation input from joypad

                elif event.type == pygame.JOYAXISMOTION:
                    axisthreshold = 0.99

                    value = event.value
                    if abs(value) > axisthreshold:

                        if event.axis == JoypadControl.AXIS1:
                            if value > 0:
                                self._horizzontalnavigation(1)
                            else:
                                self._horizzontalnavigation(-1)
                        if event.axis == 0:
                            if value > 0:
                                self._verticalnavigation(1)
                            else:
                                self._verticalnavigation(-1)

                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == JoypadControl.BUTTON0:
                        self._enter()

                elif event.type == pygame.JOYHATMOTION:
                    if event.hat == JoypadControl.DPAD:
                        self._horizzontalnavigation(event.value[0])
                        self._verticalnavigation(event.value[1])


    def _horizzontalnavigation(self, direction: int):
        self._selected = ((self._selected[0] + direction) % len(self._matrixbobs), self._selected[1])

    def _verticalnavigation(self, direction: int):
        self._selected = (self._selected[0], (self._selected[1] + direction) % len(self._matrixbobs[self._selected[0]]))

    def _enter(self):
        if self._canchoose:
            #TODO MESSAGE
            self._canchoose = False

    def setAssets(self, kwargs: Dict[str, any]):
        bobs = kwargs['bobs']

        i = 0
        for bob in bobs:
            self._modelbobs[i].append(bob)

            graphicalbob = pygame.image.load(self._mediapath + bob.id + '.png')
            self._matrixbobs[i].append(graphicalbob)

            i = (i + 1) % PyGameBobSelectionTemplate._BOBSCOLUMN


    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlistenercallback = callback
