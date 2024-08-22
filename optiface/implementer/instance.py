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
    # TODO: Alvin / Peter - can you advise on style:
    # There are many instances where we have tuple[Feature, Any]
    # There are many instances where we have dict[str, tuple[Feature, Any]]
    # Should we create a type alias for these?
    # Should we create a class for these?
    # I will refactor as part of this PR following your comments :)
    params: dict[str, tuple[Feature, Any]] = {i.name: (i, i.default) for i in FEATURES}
    instance = KnapsackInstance(params)
    instance.print_instancekey()


if __name__ == "__main__":
    main()
