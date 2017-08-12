from typing import List, Dict

from Pyro4.util import json

from foundations.dao.imodedao import IModeDAO
from model.clientgamemanage.clientmode import ClientMode


class ModeDAO(IModeDAO):
    def __init__(self):
        self._path: str = None

    def update(self, mode: ClientMode) -> ClientMode:
        pass

    def save(self, mode: ClientMode) -> ClientMode:
        pass

    def getAll(self) -> List[ClientMode]:
        clientmodelist: List[ClientMode] = list()
        with open(self._path) as data_file:
            data: List[Dict[str, any]] = json.load(data_file)

        for mode in data:
            clientmode: ClientMode = ClientMode()
            clientmode.id = mode["id"]
            clientmode.name = mode["name"]
            clientmode.dimensions = (mode["mapwidth"], mode["mapheight"])
            clientmode.duration = mode["gamedurationinseconds"]
            clientmode.numplayers = mode["maxplayers"]

            clientmodelist.append(clientmode)

        return clientmodelist

    def getByID(self, id: str) -> ClientMode:
        pass

    @property
    def filepath(self) -> str:
        return self._path

    @filepath.setter
    def filepath(self, path: str):
        self._path = path
