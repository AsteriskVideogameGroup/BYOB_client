from typing import Dict

from foundations.ioc.utils.InjContentTranslator import InjContentTranslator
from foundations.ioc.utils.InjectionSource import InjectionSource


class FEDContainer:
    def __init__(self, translator: InjContentTranslator, source: InjectionSource):
        self._objectTranslator: InjContentTranslator = translator
        self._source: InjectionSource = source
        self._translatedObjects: Dict[str, object] = dict()

        self._preloadNotLazyObjects()

    def getObject(self, objectid: str) -> object:

        requested = self._translatedObjects.get(objectid)

        if requested is None:
            requestedobjectbundle = self._objectTranslator.translate(self._source, objectid, self._translatedObjects)
            self._translatedObjects = {**self._translatedObjects, **requestedobjectbundle}
            requested = self._translatedObjects[objectid]

        return requested

    def _preloadNotLazyObjects(self):
        # fill with not lazy instantiated objects
        notlazyobjects = self._objectTranslator.translate(self._source)
        self._translatedObjects = {**self._translatedObjects, **notlazyobjects}




