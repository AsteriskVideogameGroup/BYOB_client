from inspect import getfile
from typing import Callable, Dict

import pygame
import sys


from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate


class PyGameMainMenuTemplate(ITemplate):  # TODO mettere ereditarietà dal template

    MENUELEMENTSIZE = (220, 300)
    CHARACTERSIZE = (600, 600)
    EXITSIZE = (100, 100)
    ARROWSIZE = (100, 100)
    SCREENSIZE = (1280, 720)  # TODO METTERE IN FILE DI CONFIGURAZIONE
    TITLESIZE = (1000, 100)
    EXITARROWSIZE = (50, 50)

    _PATH: str = str(getfile(self.__class__)) + "/../../../foundations/media/mainmenu/"

    def __init__(self):
        pass

    def initialize(self, screen: object, observercallback : Callable[[object, GameMessages], None]):

        self.menuelement = []
        self.screen = screen

        self.background = pygame.image.load(PyGameMainMenuTemplate._PATH + 'background.png')
        self.background = pygame.transform.scale(self.background, self.SCREENSIZE)

        self.exit = pygame.image.load(PyGameMainMenuTemplate._PATH + 'exit.png')
        self.exit = pygame.transform.scale(self.exit, self.EXITSIZE)

        self.character = pygame.image.load(PyGameMainMenuTemplate._PATH + 'character.png')
        self.character = pygame.transform.scale(self.character, self.CHARACTERSIZE)

        self.title = pygame.image.load(PyGameMainMenuTemplate._PATH +'title.png')
        self.title = pygame.transform.scale(self.title, self.TITLESIZE)

        self.genericelement = pygame.image.load(PyGameMainMenuTemplate._PATH +'menuelement.png')
        self.genericelement = pygame.transform.scale(self.genericelement, self.MENUELEMENTSIZE)

        elem1 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'quickmatch.png')
        elem2 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'rankedmatch.png')
        elem3 = pygame.image.load(PyGameMainMenuTemplate._PATH + 'comingsoon.png')

        self.menuelement.append(pygame.transform.scale(elem1, self.MENUELEMENTSIZE))
        self.menuelement.append(pygame.transform.scale(elem2, self.MENUELEMENTSIZE))
        self.menuelement.append(pygame.transform.scale(elem3, self.MENUELEMENTSIZE))

        self.elemarrow = pygame.image.load(PyGameMainMenuTemplate._PATH + 'arrow.png')
        self.elemarrow = pygame.transform.scale(self.elemarrow, self.ARROWSIZE)

        self.rotatedarrow = pygame.transform.rotate(self.elemarrow, 270)
        self.rotatedarrow = pygame.transform.scale(self.rotatedarrow, self.EXITARROWSIZE)

        self.selected = 0

    def print(self):

        zeropos = (0, 0)
        self.screen.blit(self.background, zeropos)
        self.screen.blit(self.title, zeropos)

        characterposition = (900, 130)
        self.screen.blit(self.character, characterposition)

        i = 0
        step = 50
        elementstartingposition = (70, 240)

        for element in self.menuelement:
            self.screen.blit(self.genericelement, (
            elementstartingposition[0] + i * (self.MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            self.screen.blit(element, (
            elementstartingposition[0] + i * (self.MENUELEMENTSIZE[0] + step), elementstartingposition[1]))
            i = i + 1

        exitposition = (1150, 0)
        self.screen.blit(self.exit, exitposition)

        arrowstartposition = (130, 560)
        if self.selected < 3:
            self.screen.blit(self.elemarrow, (
            arrowstartposition[0] + self.selected * (self.MENUELEMENTSIZE[0] + step), arrowstartposition[1]))
        else:
            self.screen.blit(self.rotatedarrow, (1110, 30))

    def getInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.selected = (self.selected - 1) % 4
                elif event.key == pygame.K_d:
                    self.selected = (self.selected + 1) % 4
                elif event.key == pygame.K_SPACE:
                    pass

    def setAssets(self, **kwargs: dict):
        pass

