from threading import Thread, Lock
from typing import Callable, Dict

import pygame
from pygame.time import Clock

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate
from view.viewcomposers.pygame.templates.pygamemainmenutemplate import PyGameMainMenuTemplate
from view.viewcomposers.templates import Templates
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):
    def __init__(self):
        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[object, GameMessages], None] = None


        # inizializzazione di pygame e dello schermo
        pygame.init()
        self._screen = pygame.display.set_mode((500, 500))  # TODO prendere dipensioni da file di configurazione
        self._frameratemanager: Clock = pygame.time.Clock()

        # semaforo di mutua esclusione
        self._semaphore: Lock = Lock()

        # template mostrato a schermo
        self._currenttemplate: ITemplate = None

        self._templates: Dict[Templates, ITemplate] = {
            Templates.MAINMENU: PyGameMainMenuTemplate()
        }

    def init(self, eventhandlercallback: Callable[[object, GameMessages], None]):
        self._observercallback = eventhandlercallback

        self.show(Templates.MAINMENU)

        # Thread(target=self._startloop, args=()).start() # TODO questo fa partire il loop

    def show(self, chosenview: Templates):
        # retrieve e inizializzazione del template richiesto
        requestedtemplate: ITemplate = self._templates.get(chosenview)
        requestedtemplate.initialize(self._screen, self._observercallback)

        # swap del template mostrato a video
        self._semaphore.acquire()
        self._currenttemplate = requestedtemplate
        self._semaphore.release()

    def setAssets(self, **kwargs):
        pass

    def startloop(self):
        while True:
            self._semaphore.acquire()

            self._screen.fill((0, 0, 0))  # TODO riempi di nero lo schermo

            self._currenttemplate.print()
            self._currenttemplate.getInputs()

            pygame.display.flip()
            self._frameratemanager.tick(30)

            self._semaphore.release()
