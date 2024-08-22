from typing import Any

from optiface.datamodel.feature import Feature
from optiface.implementer.featureset import FEATURES
from optiface.interface.iinstance import IInstance


class KnapsackInstance(IInstance):
    def __init__(self, parameters: dict[str, tuple[Feature, Any]]) -> None:
        super().__init__(parameters)

    def read(self) -> None:
        pass

    def print_data(self) -> None:
        pass


def main() -> None:
    params: dict[str, tuple[Feature, Any]] = {i.name: (i, i.default) for i in FEATURES}
    instance = KnapsackInstance(params)
    instance.print_instancekey()


if __name__ == "__main__":
    main()
