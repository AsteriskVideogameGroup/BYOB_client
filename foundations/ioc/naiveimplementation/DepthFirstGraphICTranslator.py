from typing import Dict, List

from foundations.ioc.utils import LibraryInporter
from foundations.ioc.utils.ConfigFields import ConfigFields
from foundations.ioc.utils.InjContentTranslator import InjContentTranslator
from foundations.ioc.utils.InjectionSource import InjectionSource


class DepthFirstGraphICTranslator(InjContentTranslator):
    def __init__(self, inporter: LibraryInporter):
        self._libraryInporter: LibraryInporter = inporter

        # temporary containers
        self._objectBase: Dict[str, object] = None
        self._sourceContent: Dict[str, Dict[str, any]] = None
        self._buildedObjects: Dict[str, object] = dict()

    def setImporter(self, inporter: LibraryInporter):
        self._libraryInporter = inporter

    def translate(self,
                  source: InjectionSource,
                  objectid: str = None,
                  objectbase: Dict[str, object] = None) -> Dict[str, object]:

        translated = dict()

        self._sourceContent = source.getContent()

        if objectbase is not None:
            self._objectBase = objectbase
        else:
            self._objectBase = dict()

        if objectid is None:
            translated = self._buildAllObjects()
        else:
            requested = self._buildObject(objectid, self._sourceContent.get(objectid))
            translated[objectid] = requested
            translated = {**translated, **self._buildedObjects}  # concatena gli oggetti creati, se esistono

        self._clear()

        return translated

    def _buildAllObjects(self) -> Dict[str, object]:

        for definitionid in self._sourceContent:
            definitionid: str

            definitioncontent: Dict[str, any] = self._sourceContent.get(definitionid)

            if not self._checkPrototypeInstantiationMode(definitioncontent):
                if self._findAlreadyCreatedObject(definitionid) is None:
                    self._buildObject(definitionid, definitioncontent)

        return self._buildedObjects

    def _buildObject(self, objname: str, definition: Dict[str, any]) -> object:

        print("instanzio {0}".format(objname))

        # inserimento dell'oggetto nella lista
        modulename: str = definition[ConfigFields.MODULE_NAME]
        classtoinstantiate: str = definition[ConfigFields.CLASS_NAME]
        newinstance = self._libraryInporter.getClassObject(classtoinstantiate, modulename)

        # se true si sta lavorando in modalità protoype
        isprototypemode = self._checkPrototypeInstantiationMode(definition)

        if not isprototypemode:
            self._buildedObjects[objname] = newinstance
        else:
            print("Building {0} as PROTOTYPE".format(objname))

        # fill degli attributi dell'oggetto appena creato

        for dependency in definition[ConfigFields.PROPERTIES_FIELD]:
            dependency: Dict[str, str]

            isvaluesetter: bool = ConfigFields.PROPERTY_VALUE in dependency
            isdependencysetter: bool = ConfigFields.PROPERTY_REFEREMENT in dependency

            if not (isdependencysetter or isvaluesetter):
                raise Exception("Not valid setter format")

            # se si sta assegnando un dato primitivo
            if isvaluesetter:
                setattr(newinstance, dependency[ConfigFields.PROPERTY_NAME],
                        dependency[ConfigFields.PROPERTY_VALUE])

            # se sis sta assegnando una dipendenza ad un altro bean
            else:

                requesteddependency: any = None
                if isinstance(dependency[ConfigFields.PROPERTY_REFEREMENT], list):

                    requesteddependency: List[object] = list()

                    for referement in dependency[ConfigFields.PROPERTY_REFEREMENT]:
                        referement: str
                        requesteddependency.append(self._resolveReferement(referement))

                elif isinstance(dependency[ConfigFields.PROPERTY_REFEREMENT], dict):

                    requesteddependency: Dict[object] = dict()

                    dependencydef: Dict[str, str] = dependency[ConfigFields.PROPERTY_REFEREMENT]

                    for referement in dependencydef:
                        referement: str
                        requesteddependency[referement] = self._resolveReferement(dependencydef[referement])

                else:
                    requesteddependency: object
                    refname: str = dependency[ConfigFields.PROPERTY_REFEREMENT]
                    requesteddependency = self._resolveReferement(refname)

                setattr(newinstance, dependency[ConfigFields.PROPERTY_NAME], requesteddependency)

        return newinstance

    def _checkPrototypeInstantiationMode(self, definition):

        isprototypemode: bool = False

        if ConfigFields.INSTANTIATION_MODE in definition:
            instancemode: str = definition[ConfigFields.INSTANTIATION_MODE]
            if instancemode == ConfigFields.PROTOTYPE_M:
                isprototypemode = True
            elif instancemode == ConfigFields.SINGLETON_M:
                isprototypemode = False
            else:
                raise Exception("Unrecognized instantiation mode")
        return isprototypemode

    def _resolveReferement(self, referement: str) -> object:
        objreferred: object = self._findAlreadyCreatedObject(referement)
        # se non è stato già creato l'oggetto da assegnare
        if objreferred is None:
            objreferred = self._buildObject(referement, self._sourceContent.get(referement))
        return objreferred

    def _findAlreadyCreatedObject(self, objectid: str) -> object:

        objreferred: object = self._objectBase.get(objectid, None)

        # controlla che l'oggetto non sia stato creato nell'ultima "passata"
        if objreferred is None:
            objreferred = self._buildedObjects.get(objectid, None)

        return objreferred

    def _clear(self):
        # empty temporary containers
        self._objectBase = None
        self._sourceContent = None
        self._buildedObjects = dict()
