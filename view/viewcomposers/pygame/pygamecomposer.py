from threading import Thread, Lock
from typing import Callable, Dict

from foundations.sysmessages.gamemessages import GameMessages
from view.viewcomposers.templates import Templates
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):

    def __init__(self):
        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[object, GameMessages, Dict[str, any]], None] = None

        self._testo: str = "iniziale"  # TODO togliere

        # semaforo di mutua esclusione
        self._semaphore: Lock = Lock()

    def init(self, eventhandlercallback: Callable[[object, GameMessages, Dict[str, any]], None]):
        self._observercallback = eventhandlercallback

        Thread(target=self._startloop, args=()).start()

    def show(self, chosenview: Templates):
        self._semaphore.acquire()
        self._testo = "testo modificato"
        print("ho modificato!")
        #sleep(10)
        self._semaphore.release()

    def setAssets(self, **kwargs):
        pass

    def _startloop(self):
        while True:
            self._semaphore.acquire()
            # print("Testo da mostrare: " + self._testo)

            # TODO mostrare il template print

            # TODO gestire i comandi da tastiera getinput

            self._semaphore.release()
