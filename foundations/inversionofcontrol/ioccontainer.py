import json
from importlib import import_module
from typing import Dict, List

from multiprocessing import Lock

from foundations.inversionofcontrol.iioccontainer import IIoCContainer


class InversionOfControlContainer(IIoCContainer):
    _MODULENAME: str = "module"
    _CLASSTOIMPORT: str = "class"

    _PROPERTYDEFINITION: str = "properties"
    _PROPERTYNAME: str = "name"
    _OBJECTIDREFERENCE: str = "ref"
    _PROPERTYPRIMITIVEVALUE: str = "value"

    _INSTANTIATIONMODE: str = "inst_mode"
    _PROTOTYPEMODE: str = "prototype"
    _SINGLETONMODE: str = "singleton"

    def __init__(self):
        self._configpath: str = None
        self._objects: Dict[object] = dict()
        self._configcontent: Dict[str, Dict[str, any]] = None

        self._mutex: Lock = Lock()

    def getObject(self, identifier: str) -> object:

        self._mutex.acquire()

        if self._configpath is None:
            raise Exception("Not initialized, use init method")

        returnobj: object = self._objects.get(identifier, None)

        if returnobj is None:
            raise Exception("Unknown object!")

        self._mutex.release()

        return returnobj

    def init(self, configpath: str) -> IIoCContainer:

        self._mutex.acquire()
        self._configpath = configpath

        # lettura da file di configurazione
        self._openConfig()

        # build degli oggetti
        self._buildAllObjects()

        self._mutex.release()

        # torna l'oggetto inizializzato
        return self

    def _buildAllObjects(self) -> None:

        for definitionid in self._configcontent:
            definitionid: str

            definitioncontent: Dict[str, any] = self._configcontent.get(definitionid)

            if not self._checkPrototypeInstantiationMode(definitioncontent):
                if self._objects.get(definitionid, None) is None:
                    self._buildObject(definitionid, definitioncontent)

    def _openConfig(self) -> None:
        with open(self._configpath) as data_file:
            self._configcontent = json.load(data_file)

    def _buildObject(self, objname: str, definition: Dict[str, any]):

        # inserimento dell'oggetto nella lista
        modulo: str = definition[InversionOfControlContainer._MODULENAME]
        classe: str = definition[InversionOfControlContainer._CLASSTOIMPORT]
        imported = import_module(modulo)
        classtoinstantiate = getattr(imported, classe)
        newinstance: object = classtoinstantiate()

        # se true si sta lavorando in modalità protoype

        isprototypemode = self._checkPrototypeInstantiationMode(definition)

        if not isprototypemode:
            self._objects[objname] = newinstance
        else:
            print("Building {0} as PROTOTYPE".format(objname))

        # fill degli attributi dell'oggetto appena creato
        for dependency in definition[InversionOfControlContainer._PROPERTYDEFINITION]:
            dependency: Dict[str, str]

            isvaluesetter: bool = InversionOfControlContainer._PROPERTYPRIMITIVEVALUE in dependency
            isdependencysetter: bool = InversionOfControlContainer._OBJECTIDREFERENCE in dependency

            if not (isdependencysetter or isvaluesetter):
                raise Exception("Not valid setter format")

            # se si sta assegnando un dato primitivo
            if isvaluesetter:
                setattr(newinstance, dependency[InversionOfControlContainer._PROPERTYNAME],
                        dependency[InversionOfControlContainer._PROPERTYPRIMITIVEVALUE])

            # se sis sta assegnando una dipendenza ad un altro bean
            else:

                requesteddependency: any = None
                if isinstance(dependency[InversionOfControlContainer._OBJECTIDREFERENCE], list):

                    requesteddependency: List[object] = list()

                    for referement in dependency[InversionOfControlContainer._OBJECTIDREFERENCE]:
                        referement: str
                        requesteddependency.append(self._resolveReferement(referement))

                elif isinstance(dependency[InversionOfControlContainer._OBJECTIDREFERENCE], dict):

                    requesteddependency: Dict[object] = dict()

                    dependencydef: Dict[str, str] = dependency[InversionOfControlContainer._OBJECTIDREFERENCE]

                    for referement in dependencydef:
                        referement: str
                        requesteddependency[referement] = self._resolveReferement(dependencydef[referement])

                else:
                    requesteddependency: object
                    refname: str = dependency[InversionOfControlContainer._OBJECTIDREFERENCE]
                    requesteddependency = self._resolveReferement(refname)

                setattr(newinstance, dependency[InversionOfControlContainer._PROPERTYNAME], requesteddependency)

        return newinstance

    def _checkPrototypeInstantiationMode(self, definition):

        isprototypemode: bool = False

        if InversionOfControlContainer._INSTANTIATIONMODE in definition:
            instancemode: str = definition[InversionOfControlContainer._INSTANTIATIONMODE]
            if instancemode == InversionOfControlContainer._PROTOTYPEMODE:
                isprototypemode = True
            elif instancemode == InversionOfControlContainer._SINGLETONMODE:
                isprototypemode = False
            else:
                raise Exception("Unrecognized instantiation mode")
        return isprototypemode

    def _resolveReferement(self, referement):
        objreferred: object = self._objects.get(referement, None)
        # se non è stato già creato l'oggetto da assegnare
        if objreferred is None:
            objreferred = self._buildObject(referement, self._configcontent.get(referement))
        return objreferred


'''if __name__ == "__main__":
    a = InversionOfControlContainer().init("config.json")

    exem: ExampleClass = a.getObject("obj1")

    exem.hamburger.print()'''
