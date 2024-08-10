from enum import Enum
from optiface.datamodel.feature import Feature, OutputNames
from optiface.datamodel.keyfeature import KeyFeature


# Implementer: define your enum types here:
# SolverType is required.
# Add any other enums you need here.
class SolverType(Enum):
    MYSOLVER = 1


# TODO: Database discussions - run id not a key, because it represents the whole row, so it is easy to cross match with metadata with the integers 0,...,n, where n is the number of rows in the results data.
RUN_ID = Feature(
    name="run_id",
    default=0,
    feature_type=int,
    output_names=OutputNames("Run ID", "r_id"),
)

SET_NAME = Feature(
    name="set_name",
    default="test",
    feature_type=str,
    output_names=OutputNames("Set Name", "s_n"),
)

INSTANCE_ID = Feature(
    name="instance_id",
    default=0,
    feature_type=int,
    output_names=OutputNames("Instance ID", "i_id"),
)


# Implementer: change this to your default.
SOLVER = Feature(
    name="solver",
    default=SolverType.MYSOLVER,
    feature_type=SolverType,
    output_names=OutputNames("Solver", "sol"),
)

# Implementer: add all your solver parameters here.
SOME_SOLVER_PARAMETER = Feature(
    name="my_solver_parameter",
    default=0,
    feature_type=int,
    output_names=OutputNames("My Solver Parameter", "m_sp"),
)

# Implementer: make sure your instance / solver features are all in the instance / solver key.
INSTANCE_KEY = KeyFeature(
    name="instance_key",
    parameters=[
        SET_NAME,
        INSTANCE_ID,
    ],
    output_names=OutputNames("Instance Key", "i_key"),
)

SOLVER_KEY = KeyFeature(
    name="solver_key",
    parameters=[
        SOLVER,
        SOME_SOLVER_PARAMETER,
    ],
    output_names=OutputNames("Solver Key", "s_key"),
)

# Implementer: add all your output features here.

OBJECTIVE = Feature(
    name="objective",
    default=-1.0,
    feature_type=float,
    output_names=OutputNames("Objective", "obj"),
)

TIME = Feature(
    name="time",
    default=-1.0,
    feature_type=float,
    output_names=OutputNames("Running Time (ms)", "t_ms"),
)

FEATURES = [
    RUN_ID,
    SET_NAME,
    INSTANCE_ID,
    SOLVER,
    OBJECTIVE,
    TIME,
]

KEYS = [
    INSTANCE_KEY,
    SOLVER_KEY,
]


def main() -> None:
    for feature in FEATURES:
        feature.print()
    for key in KEYS:
        key.print()


if __name__ == "__main__":
    main()
