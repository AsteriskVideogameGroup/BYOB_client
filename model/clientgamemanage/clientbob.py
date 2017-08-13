class ClientBob:
    def __init__(self):
        self._id: str = None
        self._name: str = None
        self._lifemodifier: int = 0
        self._speedmodifier: int = 0
        self._placeblebombsmodifier: int = 0
        self._power: str = None
        self._rangemodifier: int = 0
        self._damagemodifier: int = 0

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def lifemodifier(self) -> int:
        return self._lifemodifier

    @lifemodifier.setter
    def lifemodifier(self, value: int):
        self._lifemodifier = value

    @property
    def speedmodifier(self) -> int:
        return self._speedmodifier

    @speedmodifier.setter
    def speedmodifier(self, value: int):
        self._speedmodifier = value

    @property
    def placeblebombsmodifier(self) -> int:
        return self._placeblebombsmodifier

    @placeblebombsmodifier.setter
    def placeblebombsmodifier(self, value: int):
        self._placeblebombsmodifier = value

    @property
    def power(self) -> str:
        return self._power

    @power.setter
    def power(self, power: str):
        self._power = power

    @property
    def damagemodifier(self) -> int:
        return self._damagemodifier

    @damagemodifier.setter
    def damagemodifier(self, value: int):
        self._damagemodifier = value

    @property
    def rangemodifier(self) -> int:
        return self._rangemodifier

    @rangemodifier.setter
    def rangemodifier(self, value: int):
        self._rangemodifier = value

    def __str__(self) -> str:
        return "ID: {0}, NAME: {1}, LIVES: {2}".format(self._id, self._name, self._lifemodifier)
