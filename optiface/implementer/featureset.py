import yaml

from enum import Enum
from optiface import ui
from optiface import paths
from optiface.datamodel import feature
from typing import Type


# Implementer: define your enum types here:
# SolverType is required.
# Add any other enums you need here.
class SolverType(Enum):
    MySolver = "MySolver"


YML_FEATURE_TYPE_MAP: dict[str, Type] = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "SolverType": SolverType,
}


# TODO: this is the current base API for the feature set.
# - could be cool to call it a "Spine" or something like that, see design diagram too to make it align.
# - it would be nice if it could return the group keys for the library to use, with or without database integration overhead ?
class FeatureSet:
    def __init__(self):
        self.featureset: dict[str, feature.GroupKey] = {}

    def read_yml(self, yml_path: str) -> None:
        # TODO: discuss validation better, when discussing layers and pydantic involvement.
        # - default values need to be validated
        with open(yml_path, "r") as file:
            yml_data = yaml.safe_load(file)

            for group_name, group_data in yml_data["featureset"].items():
                group: feature.GroupKey = {}
                for feature_name, feature_data in group_data.items():
                    feature_type = YML_FEATURE_TYPE_MAP[feature_data["feature_type"]]
                    new_feature = feature.Feature(
                        name=feature_name,
                        default=feature_type(feature_data["default"]),
                        feature_type=feature_type,
                        output_names=tuple(feature_data["output_names"]),
                    )
                    group[feature_name] = new_feature

                self.featureset[group_name] = group

    @property
    def instance_key(self) -> feature.GroupKey:
        return self.featureset["instance_key"]

    @property
    def solver_key(self) -> feature.GroupKey:
        return self.featureset["solver_key"]

    def print(self) -> None:
        ui.header("Full feature set:")
        for group_name, group in self.featureset.items():
            ui.subheader(group_name)
            for _, feature in group.items():
                feature.print()


# TODO: Database discussions - run id not a key, because it represents the whole row, so it is easy to cross match with metadata with the integers 0,...,n, where n is the number of rows in the results data.

FEATURE_SET = FeatureSet()
FEATURE_SET.read_yml(paths.FEATURE_SET_YML_PATH)


def main() -> None:
    FEATURE_SET.print()


if __name__ == "__main__":
    main()
