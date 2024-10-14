import logging
from abc import ABC

from optiface import ui
from optiface.datamodel import feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ISolution(ABC):
    """
    Interface for a solution to an instance of computational problem.
    """

    def __init__(self) -> None:
        self._outputs: feature.FeatureValueDict

    def configure(self, outputs: feature.FeatureValueDict) -> None:
        self._outputs = outputs

    def reset(self) -> None:
        self._outputs = dict()

    def print_solverid(self) -> None:
        print_string: str = "; ".join(
            [f"{k}: {v[1]}" for k, v in self._outputs.items()]
        )
        ui.body(f"Solution - {print_string} [opti-face]")
