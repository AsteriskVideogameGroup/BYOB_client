from typing import Tuple


class Screen:

    def __init__(self, screenmanager: object, screenwidth: int, sceenheight: int):
        self._sceenmanager: object = screenmanager
        self._screenwidth: int = screenwidth
        self._sceenheight: int = sceenheight

    @property
    def screen(self) -> object:
        return self._sceenmanager

    @property
    def width(self) -> int:
        return self._screenwidth

    @property
    def height(self) -> int:
        return self._sceenheight

    @property
    def dimensions(self) -> Tuple[int, int]:
        return self.width, self.height
