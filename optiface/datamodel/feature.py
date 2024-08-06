import logging
import logging.config
import warnings

from typing import Any, List, Dict, Tuple, Type, Optional
from optiface import ui

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class OutputNames:
    """
    Small struct to hold all desired output names for a feature.
    """

    def __init__(
        self,
        pretty_output_name: str,
        compressed_output_name: str,
    ) -> None:
        self._pretty = pretty_output_name
        self._compressed = compressed_output_name

    @property
    def pretty(self) -> str:
        return self._pretty

    @property
    def compressed(self) -> str:
        return self._compressed


class Feature:
    """
    Struct for a schema feature.
    """

    def __init__(
        self,
        name: str = "objective",
        default: Any = 100.0,
        feature_type: Type = float,
        output_names: OutputNames = None,
        # TODO: Allowed values should be replaced by the type just being enum.
        allowed_values: List[Any] = None,
    ) -> None:
        """
        self.set_default_and_type handles type checking for default value.
        """
        self._name: str
        self._default: Any
        self._type: Type
        self._output_names: OutputNames
        self.set_names(name, output_names)
        self.set_default_and_type(default, feature_type)
        self.set_allowed_values(allowed_values)

    def print(self) -> None:
        ui.body(f"Name: {self.name}")
        ui.body(f"Type: {self.type}")
        ui.body(f"Default: {self.default}")
        ui.body(f"Pretty Output Name: {self.pretty_output_name}")
        ui.body(f"Compressed Output Name: {self.compressed_output_name}")
        ui.body(f"Allowed Values: {self.allowed_values}")

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> Type:
        return self._type

    @property
    def default(self) -> Any:
        return self._default

    @property
    def pretty_output_name(self) -> str:
        return self._output_names.pretty

    @property
    def compressed_output_name(self) -> str:
        return self._output_names.compressed

    def set_names(self, name: str, output_names: OutputNames = None) -> None:
        if name is None:
            raise TypeError("Name cannot be None")
        self._name = name
        if output_names is None:
            self._output_names = OutputNames(name, name)
        else:
            self._output_names = output_names

    def set_default_and_type(self, default: Any, feature_type: Type) -> None:
        """
        Default must:
            - not be None
            - be of type feature_type
        """
        if default is None:
            raise TypeError("Default value cannot be None")
        if type(default) != feature_type:
            raise TypeError(
                f"Default value {default} does not match feature type: {feature_type}"
            )
        self._type = type(default)
        self._default = default

    def set_allowed_values(self, allowed_values: Optional[List[Any]]) -> None:
        if allowed_values is None:
            self.allowed_values = []
            return
        # static typing says Any for the values, but we check them here
        for v in allowed_values:
            if type(v) != self._type:
                raise TypeError(
                    f"Allowed value {v} does not match feature type {self._type}"
                )
        self.allowed_values = allowed_values


def main() -> None:
    OBJ = Feature()
    SET_NAME = Feature(
        name="set_name",
        default="test",
        feature_type=str,
        output_names=OutputNames("Set Name", "sn"),
    )
    ui.header("Declaring some features")
    ui.subheader("Default Feature")
    OBJ.print()
    ui.subheader("Set Name Example Feature")
    SET_NAME.print()


if __name__ == "__main__":
    main()
