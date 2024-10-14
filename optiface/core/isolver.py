import logging

from abc import ABC
from abc import abstractmethod

from optiface import ui
from optiface.core import iinstance
from optiface.core import isolution
from optiface.datamodel import feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ISolver(ABC):
    """
    Interface for a solver that solves instances of the computational problem.
    """

    def __init__(self) -> None:
        self._parameters: feature.FeatureValueDict

    def configure(self, parameters: feature.FeatureValueDict) -> None:
        self._parameters = parameters

    def print_solverid(self) -> None:
        print_string: str = "; ".join(
            [f"{k}: {v[1]}" for k, v in self._parameters.items()]
        )
        ui.body(f"Solver - {print_string} [opti-face]")

    @abstractmethod
    def configure_from_instance(self, instance: iinstance.IInstance) -> None:
        pass

    @abstractmethod
    def solve(self) -> isolution.ISolution:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
