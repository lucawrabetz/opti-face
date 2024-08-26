from enum import Enum
from optiface.datamodel.feature import Feature
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
    output_names=("Run ID", "r_id"),
)

SET_NAME = Feature(
    name="set_name",
    default="test",
    feature_type=str,
    output_names=("Set Name", "s_n"),
)

# Implementer: parameter example for knapsack example - n number of items.
N = Feature(
    name="n",
    # TODO: decide on default for features like this - required, should not really have a default at all in a sense.
    # using -1 for now.
    default=-1,
    feature_type=int,
    output_names=("Number of Items", "n"),
)

REP = Feature(
    name="instance_rep",
    default=0,
    feature_type=int,
    output_names=("Instance Rep", "i_rep"),
)


# Implementer: change this to your default.
SOLVER = Feature(
    name="solver",
    default=SolverType.MYSOLVER,
    feature_type=SolverType,
    output_names=("Solver", "sol"),
)

# Implementer: add all your solver parameters here.
SOME_SOLVER_PARAMETER = Feature(
    name="my_solver_parameter",
    default=0,
    feature_type=int,
    output_names=("My Solver Parameter", "m_sp"),
)

# Implementer: make sure your instance / solver features are all in the instance / solver key.
INSTANCE_KEY = KeyFeature(
    name="instance_key",
    parameters=[
        SET_NAME,
        REP,
    ],
    output_names=("Instance Key", "i_key"),
)

SOLVER_KEY = KeyFeature(
    name="solver_key",
    parameters=[
        SOLVER,
        SOME_SOLVER_PARAMETER,
    ],
    output_names=("Solver Key", "s_key"),
)

# Implementer: add all your output features here.

OBJECTIVE = Feature(
    name="objective",
    default=-1.0,
    feature_type=float,
    output_names=("Objective", "obj"),
)

TIME = Feature(
    name="time",
    default=-1.0,
    feature_type=float,
    output_names=("Running Time (ms)", "t_ms"),
)

FEATURES = [
    RUN_ID,
    SET_NAME,
    N,
    REP,
    SOLVER,
    OBJECTIVE,
    TIME,
]

INSTANCE_PARAMETERS = [
    SET_NAME,
    N,
    REP,
]

SOLVER_PARAMETERS = [
    SOLVER,
]

OUTPUTS = [
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
