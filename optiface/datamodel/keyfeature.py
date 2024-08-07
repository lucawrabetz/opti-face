from optiface.datamodel.feature import Feature, OutputNames
from optiface import ui
from typing import List


class KeyFeature:
    """
    Feature for a "primary key" in db terms.
    """

    def __init__(
        self, name: str, parameters: List[Feature], output_names: OutputNames = None
    ) -> None:
        self.set_names(name, output_names)
        self.set_parameters(parameters)

    @property
    def name(self) -> str:
        return self._name

    @property
    def parameters(self) -> List[Feature]:
        return self._parameters

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

    def set_parameters(self, parameters: List[Feature]) -> None:
        self._parameters = parameters

    def print(self) -> None:
        ui.body(f"Name: {self.name}")
        ui.subheader("Parameters")
        for param in self.parameters:
            param.print()
        ui.body(f"Pretty Output Name: {self.pretty_output_name}")
        ui.body(f"Compressed Output Name: {self.compressed_output_name}")


def main():
    INSTANCE_KEY = KeyFeature(
        name="instance_key",
        parameters=[
            Feature(
                name="set_name",
                default="test",
                feature_type=str,
                output_names=OutputNames("Set Name", "sn"),
            )
        ],
        output_names=OutputNames("Instance Key", "InstKey"),
    )
    ui.header("Declaring a Key Feature")
    ui.subheader("Instance Key Example Feature")
    INSTANCE_KEY.print()


if __name__ == "__main__":
    main()
