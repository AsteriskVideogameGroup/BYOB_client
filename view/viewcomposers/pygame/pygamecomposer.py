from typing import Callable

from view.viewcomposers.enumviews import EnumViews
from view.viewcomposers.iviewcomposer import IViewComposer


class PyGameComposer(IViewComposer):
    def __init__(self):

        # procedura da chiamare per notificare un evento
        self._observercallback: Callable[[str], None] = None

    def init(self, eventhandlercallback: Callable[[str], None]):
        self._observercallback = eventhandlercallback


    def show(self, chosenview: EnumViews):
        pass
