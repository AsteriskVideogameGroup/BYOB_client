from typing import Tuple


class Screen:

    def __init__(self, screenmanager: object, screenwidth: int, screenheight: int, fps: int):
        self._sceenmanager: object = screenmanager
        self._screenwidth: int = screenwidth
        self._screenheight: int = screenheight
        self._fps: int = fps

    @property
    def screen(self) -> object:
        return self._sceenmanager

    @property
    def width(self) -> int:
        return self._screenwidth

    @property
    def height(self) -> int:
        return self._screenheight

    @property
    def dimensions(self) -> Tuple[int, int]:
        return self.width, self.height

    @property
    def fps(self) -> int:
        return self._fps

