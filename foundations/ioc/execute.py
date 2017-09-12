from FEDContainer import FEDContainer
from exampleobjects.objmodule import ExampleClass
from naiveimplementation.DepthFirstGraphICTranslator import DepthFirstGraphICTranslator
from naiveimplementation.JSONSource import JSONSource
from naiveimplementation.NaiveLibraryImporter import NaiveLibraryImporter
from utils import InjContentTranslator, InjectionSource
from utils.LibraryInporter import LibraryImporter

if __name__ == "__main__":

    imp: LibraryImporter = NaiveLibraryImporter()

    # source
    source: InjectionSource = JSONSource("config.json")

    #duck = imp.getClassObject("Duck", "exampleobjects.simpleexample")
    #duck.quack()

    #print(source.getContent())

    trans: InjContentTranslator = DepthFirstGraphICTranslator(imp)
    #a = trans.translate(source, "obj3")
    #print(a)

    test: ExampleClass = FEDContainer(trans, source).getObject("obj1")

    test.print()