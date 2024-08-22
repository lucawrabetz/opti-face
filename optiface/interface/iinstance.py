import logging
import os

from abc import ABC
from abc import abstractmethod
from typing import Any

from optiface import ui
from optiface.datamodel import Feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IInstance(ABC):
    """
    Interface for an instance of the computational problem.
    """

    def __init__(self, set_name: str, rep: int):
        self._set_name: str = set_name
        self._rep: int = rep
        # TODO: see issue #17.
        self._parameters: dict[Feature, Any]
        self._filename: str
        self.set_filename()

    def set_filename(self):
        param_string = "_".join([v for v in self._parameters.values()])
        self._filename = "-".join([self._set_name, param_string, str(self._rep)])

    @property
    def set_name(self):
        return self._set_name

    @property
    def rep(self):
        return self._rep

    @property
    def filepath(self):
        return os.path.join(self._filename, ".csv")

    @abstractmethod
    def read(self):
        pass
