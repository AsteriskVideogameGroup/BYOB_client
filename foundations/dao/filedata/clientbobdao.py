import json
from typing import List, Dict

from foundations.dao.iclientbobdao import IClientBobDAO
from model.gamemanage.clientbob import ClientBob


class ClientBobDAO(IClientBobDAO):
    def __init__(self):
        self._path: str = None

    def getAll(self) -> List[ClientBob]:
        clientmodelist: List[ClientBob] = list()
        with open(self._path) as data_file:
            data: List[Dict[str, any]] = json.load(data_file)

        for bobpersistent in data:
            bob: ClientBob = ClientBob()
            bob.id = bobpersistent["id"]
            bob.name = bobpersistent["name"]
            bob.damagemodifier = bobpersistent["damagemodifier"]
            bob.placeblebombsmodifier = bobpersistent["placeblebombsmodifier"]
            bob.lifemodifier = bobpersistent["lifemodifier"]
            bob.speedmodifier = bobpersistent["speedmodifier"]
            bob.power = bobpersistent["powerid"]
            bob.rangemodifier = bobpersistent["range"]

            clientmodelist.append(bob)

        return clientmodelist

    @property
    def filepath(self) -> str:
        return self._path

    @filepath.setter
    def filepath(self, path: str):
        self._path = path
