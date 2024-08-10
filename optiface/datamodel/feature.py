import logging
import warnings

from optiface import ui
from typing import Any, Dict, List, Optional, Tuple, Type

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

    def print(self) -> None:
        ui.body(f"Name: {self.name}")
        ui.body(f"Type: {self.type}")
        ui.body(f"Default: {self.default}")
        ui.body(f"Pretty Output Name: {self.pretty_output_name}")
        ui.body(f"Compressed Output Name: {self.compressed_output_name}")
        ui.blank_line()

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
