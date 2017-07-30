import abc

from view.viewcomposers.viewsnames import ViewNames


class IViewTemplateAbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getTemplate(self, templateid: ViewNames):
        pass
