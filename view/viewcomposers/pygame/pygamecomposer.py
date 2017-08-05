from threading import Lock
from typing import Callable, Dict

import pygame
from pygame.time import Clock

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate
from view.viewcomposers.pygame.templates.pgmainmenutemplate import PyGameMainMenuTemplate
from view.viewcomposers.pygame.templates.pggameselectiontemplate import PyGameGameSelectionTemplate
from view.viewcomposers.templates import Templates
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):
    def __init__(self):
        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[object, GameMessages], None] = None

        # inizializzazione di pygame e dello schermo
        pygame.init()

        # dati di screen
        # TODO prendere dipensioni da file di configurazione
        width = 1280
        height = 720
        screenobject: object = pygame.display.set_mode((width, height))
        # TODO prendere dipensioni da file di configurazione
        self._screen: Screen = Screen(screenobject, width, height)

        self._frameratemanager: Clock = pygame.time.Clock()
        self._framerate: int = 60  # TODO prendere framerate da file di configurazione

        # path base per i media
        self._basemediapath: str = "foundations/media/"  # TODO prendere da file di configurazione

        # inizializzazione joypad
        self._initJoyPad()

        # semaforo di mutua esclusione
        self._semaphore: Lock = Lock()

        # template mostrato a schermo
        self._currenttemplate: ITemplate = None

        # template disponibili
        self._templates: Dict[Templates, ITemplate] = {
            Templates.MAINMENU: PyGameMainMenuTemplate(),
            Templates.GAMESELECTION: PyGameGameSelectionTemplate()
        }

    def init(self, eventhandlercallback: Callable[[object, GameMessages], None]):
        self._observercallback = eventhandlercallback

    def show(self, chosenview: Templates):
        # retrieve e inizializzazione del template richiesto
        requestedtemplate: ITemplate = self._templates.get(chosenview)
        requestedtemplate.initialize(self._screen, self._basemediapath, self._observercallback)
        print("sto cambiando")

        # swap del template mostrato a video
        self._semaphore.acquire()  # TODO vedere come non fare un macello con i deadlock
        self._currenttemplate = requestedtemplate
        print("ho cambiato")
        self._semaphore.release()

    def setAssets(self, **kwargs):
        self._semaphore.acquire()
        self._currenttemplate.setAssets(kwargs)
        self._semaphore.release()

        pass

    def startWorking(self):
        while True:
            screen: pygame.Surface = self._screen.screen
            screen.fill((0, 0, 0))  # TODO riempi di nero lo schermo

            self._semaphore.acquire()
            self._currenttemplate.print()
            self._semaphore.release()
            self._currenttemplate.getInputs()

            pygame.display.flip()
            self._frameratemanager.tick(self._framerate)

    def _initJoyPad(self):
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        if joysticks:
            joysticks[0].init()
