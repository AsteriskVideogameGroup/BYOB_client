import abc

from view.viewcomposers.enumviews import EnumViews


class IViewTemplateAbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getTemplate(self, templateid: EnumViews):
        pass
