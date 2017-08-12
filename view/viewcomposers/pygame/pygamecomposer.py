from threading import Lock
from typing import Callable, Dict

import pygame
from pygame.time import Clock

from foundations.screenutils.screen import Screen
from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.itemplate import ITemplate
from view.viewcomposers.pygame.templates.pgbobselectiontemplate import PyGameBobSelectionTemplate
from view.viewcomposers.pygame.templates.pggamewaitingtemplate import PyGameGameWaitingTemplate
from view.viewcomposers.pygame.templates.pgmainmenutemplate import PyGameMainMenuTemplate
from view.viewcomposers.pygame.templates.pgmodeselectiontemplate import PyGameModeSelectionTemplate
from view.viewcomposers.templates import Templates
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):
    def __init__(self):
        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[object, GameMessages, Dict[str, any]], None] = None

        # inizializzazione di pygame e dello schermo
        pygame.init()

        # settings di finestra
        self._windowname: str = None
        self._windowwidth: int = 0
        self._windowheight: int = 0
        self._framerate: int = 0
        self._frameratemanager: Clock = pygame.time.Clock()
        self._screen: Screen = None

        # inizializzazione joypad
        self._initJoyPad()

        # path dei media content
        self._basemediapath: str = None

        # template disponibili
        self._templates: Dict[Templates, ITemplate] = {
            Templates.MAINMENU: PyGameMainMenuTemplate(),
            Templates.GAMESELECTION: PyGameModeSelectionTemplate(),
            Templates.GAMEWAIT: PyGameGameWaitingTemplate(),
            Templates.CHOOSEBOB: PyGameBobSelectionTemplate()
        }

        # template mostrato a schermo correntemente
        self._currenttemplate: ITemplate = None

        # semaforo di mutua esclusione (gestione multithreading)
        self._semaphore: Lock = Lock()

    def init(self, eventhandlercallback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._observercallback = eventhandlercallback

        # bundle dello screen
        screenobject: object = pygame.display.set_mode((self._windowwidth, self._windowheight))
        self._screen = Screen(screenobject, self._windowwidth, self._windowheight, self._framerate)

        # mostra titolo finestra
        pygame.display.set_caption(self._windowname)

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

    def setAssets(self, kwargs: Dict[str, any]):
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

    @property
    def windowcaption(self) -> str:
        return self._windowname

    @windowcaption.setter
    def windowcaption(self, cap: str):
        self._windowname = cap

    @property
    def windowwidth(self) -> int:
        return self._windowwidth

    @windowwidth.setter
    def windowwidth(self, width: int):
        self._windowwidth = width

    @property
    def windowheight(self) -> int:
        return self._windowheight

    @windowheight.setter
    def windowheight(self, height: int):
        self._windowheight = height

    @property
    def framerate(self) -> int:
        return self._windowheight

    @framerate.setter
    def framerate(self, fr: int):
        self._framerate = fr

    @property
    def mediapath(self) -> str:
        return self._basemediapath

    @mediapath.setter
    def mediapath(self, path: str):
        self._basemediapath = path