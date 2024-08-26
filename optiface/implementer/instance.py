import os
from typing import Any

from optiface.datamodel.feature import Feature, FeatureDict
from optiface.implementer.featureset import FEATURES
from optiface.interface.iinstance import IInstance
from optiface.paths import _DAT_DIR


class KnapsackInstance(IInstance):
    """
    Class for an instance of the knapsack problem (https://en.wikipedia.org/wiki/Knapsack_problem), specifically the 0-1 knapsack problem.
        - Parameters: n - number of items.
        - Data: weights (n integers), values (n integers), capacity (integer).
    """

    def __init__(self, parameters: FeatureDict) -> None:
        super().__init__(parameters)
        self._weights: list[int]
        self._values: list[int]
        self._capacity: int

    def read(self) -> None:
        # TODO: assuming for now we always read from a csv file, we will generalize this a bit or give space for more options with this contract.
        file_extension = ".csv"
        file_path = os.path.join(_DAT_DIR, self.filename + file_extension)
        pass

    def print_data(self) -> None:
        pass


def main() -> None:
    params: FeatureDict = {i.name: (i, i.default) for i in FEATURES}
    instance = KnapsackInstance(params)
    instance.print_instancekey()


if __name__ == "__main__":
    main()
