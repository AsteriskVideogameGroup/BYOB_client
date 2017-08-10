import json
from importlib import import_module
from typing import Dict

from foundations.inversionofcontrol.idicontainer import IDependencyInjectionContainer


class DepInjContainer(IDependencyInjectionContainer):

    _MODULENAME: str = "module"
    _CLASSTOIMPORT: str = "class"

    _PROPERTYDEFINITION: str = "properties"
    _PROPERTYNAME: str = "name"
    _OBJECTIDREFERENCE: str = "ref"
    _PROPERTYPRIMITIVEVALUE: str = "value"

    def __init__(self):
        self._configpath: str = None
        self._objects: Dict[object] = dict()
        self._configcontent: Dict[str, Dict[str, any]] = None

    def getObject(self, id: str) -> object:
        if self._configpath is None:
            raise Exception("Not initialized, use init method")

        returnobj: object = self._objects.get(id, None)

        if returnobj is None:
            raise Exception("Unknown object!")

        return returnobj

    def init(self, configpath: str) -> IDependencyInjectionContainer:
        self._configpath = configpath

        # lettura da file di configurazione
        self._openConfig()

        # build degli oggetti
        self._buildAllObjects()

        # torna l'oggetto inizializzato
        return self

    def _buildAllObjects(self) -> None:

        for bean in self._configcontent:
            bean: str
            # self._configcontent[bean]["mark"] = False

            if self._objects.get(bean, None) is None:
                self._build(bean, self._configcontent.get(bean))

    def _openConfig(self) -> None:
        with open(self._configpath) as data_file:
            self._configcontent = json.load(data_file)

    def _build(self, beanname: str, bean: Dict[str, any]):

        # inserimento dell'oggetto nella lista
        modulo: str = bean[DepInjContainer._MODULENAME]
        classe: str = bean[DepInjContainer._CLASSTOIMPORT]
        imported = import_module(modulo)
        classtoinstantiate = getattr(imported, classe)
        newinstance: object = classtoinstantiate()
        self._objects[beanname] = newinstance

        # fill degli attributi dell'oggetto appena creato
        for dependency in bean[DepInjContainer._PROPERTYDEFINITION]:
            dependency: Dict[str, str]

            isvaluesetter: bool = DepInjContainer._PROPERTYPRIMITIVEVALUE in dependency
            isdependencysetter: bool = DepInjContainer._OBJECTIDREFERENCE in dependency

            if not (isdependencysetter or isvaluesetter):
                raise Exception("Not valid setter format")

            # se si sta assegnando un dato primitivo
            if isvaluesetter:

                setattr(newinstance, dependency[DepInjContainer._PROPERTYNAME], dependency[DepInjContainer._PROPERTYPRIMITIVEVALUE])

            # se sis sta assegnando una dipendenza ad un altro bean
            else:
                objreferred: object = self._objects.get(dependency[DepInjContainer._OBJECTIDREFERENCE], None)

                # se non è stato già creato l'oggetto da assegnare
                if objreferred is None:
                    refname: str = dependency[DepInjContainer._OBJECTIDREFERENCE]
                    objreferred: object = self._build(refname, self._configcontent.get(refname))

                setattr(newinstance, dependency[DepInjContainer._PROPERTYNAME], objreferred)

        return newinstance


'''if __name__ == "__main__":
    a = DepInjContainer().init("config.json")

    exem: ExampleClass = a.getObject("obj1")

    exem.hamburger.print()'''
