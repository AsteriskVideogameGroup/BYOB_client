import abc
from typing import Dict

from foundations.easy_dependency_injection.utils import LibraryInporter

from foundations.ioc.utils.InjectionSource import InjectionSource


class InjContentTranslator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def translate(self,
                  source: InjectionSource,
                  objectid: str = None,
                  objectbase: Dict[str, object] = None) -> Dict[str, object]:
        pass

    @abc.abstractmethod
    def setImporter(self, importer: LibraryInporter):
        pass