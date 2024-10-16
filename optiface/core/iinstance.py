import logging
import os

from abc import ABC
from abc import abstractmethod
from typing import Any

from optiface import ui
from optiface.datamodel import feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IInstance(ABC):
    """
    Interface for an instance of the computational problem.
    """

    def __init__(self):
        self._parameters: feature.FeatureValueDict
        self._filepath: str

    def __str__(self) -> str:
        return f"Instance: {'; '.join([f'{k}: {v[1]}' for k, v in self._parameters.items()])}"

    def configure(
        self, parameters: feature.FeatureValueDict, filepath: str = ""
    ) -> None:
        # TODO (LW / PS): I think make sure set_name is first parameter and rep is last parameter (out of instance parameters). Related - enforcing required / starting parameters (starting schema), but not let anyone change it, and certain orders either.
        # TODO (LW / PS): align parameters with featureset - see issue #17.
        self._parameters = parameters
        self._filepath = filepath
        if self._filepath == "":
            ui.body(f"Configuring unsaved instance [opti-face]:")
            ui.body(self.__str__())
        else:
            ui.body(f"Configuring instance from {filepath} [opti-face]:")
            ui.body(self.__str__())

    @property
    def filepath(self) -> str:
        return self._filepath

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
