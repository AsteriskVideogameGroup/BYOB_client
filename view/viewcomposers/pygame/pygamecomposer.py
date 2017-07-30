from threading import Semaphore, Thread
from typing import Callable

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.viewsnames import ViewNames
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):
    def __init__(self):
        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[str], None] = None

        self._testo: str = "iniziale"

        # semaforo di mutua esclusione
        self._semaphore: Semaphore = Semaphore()

    def init(self, eventhandlercallback: Callable[[object, GameMessages], None]):
        self._observercallback = eventhandlercallback

        Thread(target=self._startloop, args=()).start()

    def show(self, chosenview: ViewNames):
        self._semaphore.acquire()
        self._testo = "testo modificato"
        self._semaphore.release()

    def _startloop(self):
        while True:
            self._semaphore.acquire()
            print("Testo da mostrare: " + self._testo)
            self._semaphore.release()
