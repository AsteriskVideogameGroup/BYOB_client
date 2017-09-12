class ConfigFields:

    # class definition
    MODULE_NAME: str = "module"
    CLASS_NAME: str = "class"

    # instantiation mode
    INSTANTIATION_MODE: str = "inst_mode"
    PROTOTYPE_M: str = "prototype"
    SINGLETON_M: str = "singleton"

    # properties field
    PROPERTIES_FIELD: str = "properties"
    PROPERTY_NAME: str = "name"
    PROPERTY_REFEREMENT: str = "ref"
    PROPERTY_VALUE: str = "value"

    def __init__(self):
        raise TypeError("Cannot create {0} instances".format(self.__class__))
