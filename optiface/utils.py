from datetime import datetime
import os

from gurobipy import Model

from optiface.constants import _DATE_FORMAT, _DATETIME_FORMAT
from optiface.paths import _LOGS_DIR


def append_date(base: str, time: bool = True) -> str:
    """
    Append today's date to base string.
    """
    today = datetime.now()
    if time:
        date_str = today.strftime(_DATETIME_FORMAT)
    else:
        date_str = today.strftime(_DATE_FORMAT)
    name = base + "-" + date_str
    return name


def throwaway_gurobi_model() -> None:
    """
    Create an empty gurobi model and destroy it.
    This is a hacky workaround to get rid of the dreaded "academic license", and "set parameter username" printouts from gurobi which also print twice in this case because of the log config. These only print the first time gurobi is called in memory. Just call this function from any class that runs a series of gurobi models in the __init__ method to ensure your logging works as expected and is readable.
    """
    model = Model("fake")
    del model


def gurobi_log_file() -> str:
    if not os.path.exists(_LOGS_DIR):
        os.makedirs(_LOGS_DIR)
    basename: str = "gurobi"
    filename: str = append_date(basename, time=True) + ".log"
    filepath: str = os.path.join(_LOGS_DIR, filename)
    return filepath
