from importlib import import_module

from foundations.ioc.utils.LibraryInporter import LibraryImporter


class NaiveLibraryImporter(LibraryImporter):

    def getClassObject(self, classname: str, modulename: str) -> object:

        # import the module
        imported = import_module(modulename)
        # get the class ref
        classtoinstantiate = getattr(imported, classname)

        return classtoinstantiate()


