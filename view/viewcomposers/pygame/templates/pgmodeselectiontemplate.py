import os
from inspect import getfile
from typing import Callable, Dict

import pygame
import sys

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from foundations.joypadsupport.joypadcontrol import JoypadControl
from view.viewcomposers.itemplate import ITemplate

class PyGameModeSelectionTemplate:#(ITemplate):

    #DEVE CONOSCERE:
    #- Tipo di match (ranked o no)
    #- Elenco di descrizioni di modalità (in un dict) con i seguenti attributi:
    #  0) Nome
    #  1) Durata partita
    #  2) Numero giocatori
    #  3) Dimensioni della mappa
    #


    _ARROWSIZE = (70, 70)
    _SELECTABLEITEMS = 3
    _NAMEFRAMESIZE = (700, 100)
    _DESCRIPTIONSIZE = (700, 300)
    _BUTTONSSIZE = (200,50)

    _MEDIAPATH = "modeselection/"
    _FONTPATH = "font/"

    def __init__(self):
        self._menuelement = []
        self._eventlistnercallback = None
        self._screen = None
        self._modes = []
        self._ranked = False
        self._selected = 0
        self._currentMode = 0
        self._modesnames = []

    def initialize(self, screen: Screen, mediapath: str, observercallback: Callable[[object, GameMessages, Dict[str, any]], None]):

        WHITE = (255,255,255)

        pygame.font.init()
        font_path = mediapath + PyGameModeSelectionTemplate._FONTPATH+"Emulogic/emulogic.ttf"
        font_name_size = 24
        font_description_size = 18
        self.mediapath = mediapath + PyGameModeSelectionTemplate._MEDIAPATH

        self._font_description = pygame.font.Font(font_path, font_description_size)
        self._font_name = pygame.font.Font(font_path, font_name_size)

        self._screen = screen.screen
        self._screendims = screen.dimensions
        self.registerEventListener(observercallback)

        # Background loading and resizing

        self._background = pygame.image.load(self.mediapath + 'background.png')
        self._background = pygame.transform.scale(self._background, self._screendims)

        # Title
        if self._ranked:
            title = "ranked match"
        else:
            title = "quick match"
        font_title_size = 24
        self._font_title = pygame.font.Font(font_path, font_title_size)


        self._title = self._font_title.render(title + " - mode selection", 1, WHITE)

        # Name frame picture loading and resizing
        self._nameframe = pygame.image.load(self.mediapath + 'modenameframe.png')
        self._nameframe = pygame.transform.scale(self._nameframe, PyGameModeSelectionTemplate._NAMEFRAMESIZE)

        # Description frame picture loading and resizing
        self._descriptionframe = pygame.image.load(self.mediapath + 'descriptionframe.png')
        self._descriptionframe = pygame.transform.scale(self._descriptionframe, PyGameModeSelectionTemplate._DESCRIPTIONSIZE)


        # Menu cursor icon loading and resizing

        self._elemarrow = pygame.image.load(self.mediapath + 'arrow.png')
        self._elemarrow = pygame.transform.scale(self._elemarrow, PyGameModeSelectionTemplate._ARROWSIZE)


        # Buttons

        self._matchmakingbutton = pygame.image.load(self.mediapath + 'findmatchbutton.png')
        self._matchmakingbutton = pygame.transform.scale(self._matchmakingbutton, PyGameModeSelectionTemplate._BUTTONSSIZE)
        self._backbutton = pygame.image.load(self.mediapath + 'backbutton.png')
        self._backbutton = pygame.transform.scale(self._backbutton, PyGameModeSelectionTemplate._BUTTONSSIZE)




    def print(self):

        framestep = 30

        # Background and title positioning and print

        zeropos = (0, 0)
        self._screen.blit(self._background, zeropos)

        titleposition = ((self._screendims[0] - self._title.get_rect().width)/2,
                         self._screendims[1]/20)
        self._screen.blit(self._title, titleposition)

        nameframeposition = ((self._screendims[0] - PyGameModeSelectionTemplate._NAMEFRAMESIZE[0])/2,130)
        self._screen.blit(self._nameframe, nameframeposition)

        descriptionframeposition = ((self._screendims[0] - PyGameModeSelectionTemplate._NAMEFRAMESIZE[0])/2,
                                    nameframeposition[1] + PyGameModeSelectionTemplate._NAMEFRAMESIZE[1]+ framestep)
        self._screen.blit(self._descriptionframe, descriptionframeposition)



        # Current mode details

        BLACK = (0,0,0)
        namelabel = self._font_name.render(self._modes[self._currentMode]['name'], 1, BLACK)
        textwidth = namelabel.get_rect().width
        textheight = namelabel.get_rect().height
        nameposition = (nameframeposition[0]+(self._NAMEFRAMESIZE[0]-textwidth)/2,
                        nameframeposition[1]+(self._NAMEFRAMESIZE[1]-textheight)/2)
        self._screen.blit(namelabel, nameposition)

        numplayerstring = "players: " + str(self._modes[self._currentMode]['numplayers'])
        durationstring = "time: "+ str(self._modes[self._currentMode]['duration'])+" mins"
        mapdimensionsstring = "Map size: "+ str(self._modes[self._currentMode]['dimensions'][0]) + "x" \
                              + str(self._modes[self._currentMode]['dimensions'][1])


        numplayerlabel = self._font_description.render(numplayerstring,1,BLACK)
        numplayerheight = numplayerlabel.get_rect().height
        numplayerposition = (descriptionframeposition[0]+descriptionframeposition[0]/7,
                             descriptionframeposition[1] + (PyGameModeSelectionTemplate._DESCRIPTIONSIZE[1]-numplayerheight)/4)

        self._screen.blit(numplayerlabel,numplayerposition)


        durationlabel = self._font_description.render(durationstring,1,BLACK)
        durationheight = durationlabel.get_rect().height
        durationposition = (numplayerposition[0],
                             numplayerposition[1] + (PyGameModeSelectionTemplate._DESCRIPTIONSIZE[1]-durationheight)/5)

        self._screen.blit(durationlabel,durationposition)


        mapdimensionslabel = self._font_description.render(mapdimensionsstring,1,BLACK)
        mapdimensionsheight = mapdimensionslabel.get_rect().height
        mapdimensionsposition = (numplayerposition[0],
                             durationposition[1] + (PyGameModeSelectionTemplate._DESCRIPTIONSIZE[1]-mapdimensionsheight)/5)

        self._screen.blit(mapdimensionslabel,mapdimensionsposition)


        # Buttons
        backbuttonposition = (nameframeposition[0],
                              descriptionframeposition[1]+PyGameModeSelectionTemplate._DESCRIPTIONSIZE[1]+framestep)
        matchmakingbuttonposition = (nameframeposition[0]+PyGameModeSelectionTemplate._NAMEFRAMESIZE[0]-PyGameModeSelectionTemplate._BUTTONSSIZE[0],
                              descriptionframeposition[1]+PyGameModeSelectionTemplate._DESCRIPTIONSIZE[1]+framestep)
        self._screen.blit(self._backbutton, backbuttonposition)
        self._screen.blit(self._matchmakingbutton, matchmakingbuttonposition)






        # Cursor positioning and print

        cursorposition = (0,0)

        if self._selected == 0:
            cursorposition = (nameframeposition[0] + PyGameModeSelectionTemplate._NAMEFRAMESIZE[0]/2 - PyGameModeSelectionTemplate._ARROWSIZE[0]/2,
                              nameframeposition[1] + PyGameModeSelectionTemplate._NAMEFRAMESIZE[1] - 30)
        elif self._selected == 2:
            cursorposition = (backbuttonposition[0] + PyGameModeSelectionTemplate._BUTTONSSIZE[0]/2 - PyGameModeSelectionTemplate._ARROWSIZE[0]/2,
                              backbuttonposition[1] + PyGameModeSelectionTemplate._BUTTONSSIZE[1] - 15)
        else:
            cursorposition = (matchmakingbuttonposition[0] + PyGameModeSelectionTemplate._BUTTONSSIZE[0]/2 - PyGameModeSelectionTemplate._ARROWSIZE[0]/2,
                              matchmakingbuttonposition[1] + PyGameModeSelectionTemplate._BUTTONSSIZE[1] - 15)
        self._screen.blit(self._elemarrow, cursorposition)



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
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._select(-1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._select(1)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    self._horizzontalnavigation(-1)
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    self._horizzontalnavigation(1)

                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self._enter()

            # Joypad commands:
            # AXIS0 to right, DPAD right: cursor to right (circularly)
            # AXIS0 to left, DPAD left: cursor to left (circularly)
            # Button0: selection

            elif event.type == pygame.JOYAXISMOTION:
                value = event.value
                if abs(value) > axisthreshold:

                    if event.axis == JoypadControl.AXIS1:

                        if value > 0:
                            self._select(1)
                        else:
                            self._select(-1)
                    if event.axis == 0:
                        if value > 0:
                            self._horizzontalnavigation(1)
                        else:
                            self._horizzontalnavigation(-1)




            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == JoypadControl.BUTTON0:
                    self._enter()

            elif event.type == pygame.JOYHATMOTION:
                if event.hat == JoypadControl.DPAD:
                    self._select(-event.value[1])
                    if abs(event.value[0]):
                        if event.value[0] > 0:
                            self._horizzontalnavigation(1)
                        else:
                            self._horizzontalnavigation(-1)

    def _horizzontalnavigation(self, direction : int):
        if direction > 0:
            leftrightexception = 2
        else:
            leftrightexception = 1

        if self._selected == 0:
            self._modelooking(direction)
        elif self._selected == leftrightexception:
            self._select(-direction)

    def _modelooking(self, direction : int):
        self._currentMode = (self._currentMode + direction) % len(self._modes)

    def _enter(self):
        if self._selected == 0:
            self._selected = 2
        elif self._selected == 1:
            self._eventlistnercallback(GameMessages.PREVIOUS)
        else:
            if not self._ranked:
                self._eventlistnercallback(GameMessages.INITUNRANKEDGAME,)
            else:
                self._eventlistnercallback(GameMessages.INITRANKEDGAME)

    def _select(self, direction: int):

        # Move the cursor of 'direction' positions to right (can be negative) circularly

        self._selected = (self._selected + direction) % PyGameModeSelectionTemplate._SELECTABLEITEMS

    def setAssets(self, kwargs: dict):
        self._modes = kwargs['modes']
        self._currentMode = 0
        self._ranked = kwargs['ranked']


    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._eventlistnercallback = callback
