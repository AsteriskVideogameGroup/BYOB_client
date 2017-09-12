import json
from typing import Dict

from foundations.ioc.utils.DataSource import DataSource
from foundations.ioc.utils.InjectionSource import InjectionSource


class JSONSource(InjectionSource, DataSource):
    def __init__(self, uri: str):
        self._uri: str = ""
        self.open(uri)

        self._content: Dict[str, Dict[str, any]] = None

    def close(self):
        print("File {0} closed".format(self._uri))

    def getContent(self) -> Dict[str, Dict[str, any]]:
        if self._content is None:
            self._content = self._opencontent(self._uri)

        return self._content

    def open(self, uri: str):
        self._uri = uri
        print("File {0} open".format(self._uri))

    def getURI(self) -> str:
        return self._uri

    def _opencontent(self, uri: str) -> Dict[str, Dict[str, any]]:
        content = None
        with open(uri) as data_file:
            content = json.load(data_file)

        return content
