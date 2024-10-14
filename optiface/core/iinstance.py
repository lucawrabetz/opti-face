import logging

from abc import ABC
from abc import abstractmethod

from optiface import ui
from optiface.datamodel import feature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IInstance(ABC):
    """
    Interface for an instance of the computational problem.
    """

    def configure(
        self, parameters: feature.FeatureValueDict, filepath: str = ""
    ) -> None:
        # TODO (LW / PS): I think make sure set_name is first parameter and rep is last parameter (out of instance parameters). Related - enforcing required / starting parameters (starting schema), but not let anyone change it, and certain orders either.
        # re: above - not sure if this is necessary - the structure of all three classes ISolver, IInstance, and ISolution having a member _parameters (or _outputs for ISolution) being a FeatureValueDict allows us to defer the dependency on implementer declarations to the higher layer, which is what we want. We should address the comments above and below this one together and we should be fine to not worry about "starter" features, or to not explicityly refer to them in this layer at least.
        # TODO (LW / PS): align parameters with featureset - see issue #17.
        self._parameters: feature.FeatureValueDict = parameters
        self._filepath: str = filepath
        if self._filepath == "":
            ui.body(f"Configuring unsaved instance [opti-face]:")
            self.print_instanceid()
        else:
            ui.body(f"Configuring instance from {filepath} [opti-face]:")

    @property
    def filepath(self) -> str:
        return self._filepath

    def print_instanceid(self) -> None:
        print_string: str = "; ".join(
            [f"{k}: {v[1]}" for k, v in self._parameters.items()]
        )
        ui.body(f"Instance - {print_string} [opti-face]")

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def print_data(self) -> None:
        pass
