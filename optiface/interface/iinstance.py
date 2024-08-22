import logging
import os

from abc import ABC
from abc import abstractmethod
from typing import Any

from optiface import ui
from optiface.datamodel.feature import Feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IInstance(ABC):
    """
    Interface for an instance of the computational problem.
    """

    def __init__(self, parameters: dict[str, tuple[Feature, Any]]):
        # TODO (LW / PS): I think make sure set_name is first parameter and rep is last parameter (out of instance parameters). Related - enforcing required / starting parameters (starting schema), but not let anyone change it, and certain orders either.
        # TODO (LW / PS): align parameters with featureset - see issue #17.
        self._parameters: dict[str, tuple[Feature, Any]] = parameters
        self._filename: str
        self.set_filename()

    def set_filename(self):
        self._filename = "_".join([v[1] for v in self._parameters.values()])

    @property
    def filename(self):
        return self._filename

    def print_instancekey(self):
        print_string = "; ".join([f"{k}: {v[1]}" for k, v in self._parameters.items()])
        ui.body(f"Instance - {print_string}")

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def print_data(self):
        pass
