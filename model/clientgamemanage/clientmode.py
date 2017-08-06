class ClientMode:

    def __init__(self):
        self._id: str = None
        self._name: str = None
        self._numplayers: int = 0
        self._duration: int = 0
        self._dimensions: (int, int) = (0, 0)

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
    def numplayers(self) -> int:
        return self._numplayers

    @numplayers.setter
    def numplayers(self, value: int):
        self._numplayers = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int):
        self._duration = value

    @property
    def dimensions(self) -> (int, int):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value: (int, int)):
        self._dimensions = value

