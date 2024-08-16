import os

# TODO: should this be on one of the problem classes, or as well, or removed from here.
_FORKNAME = "onlinekcenter"
_DAT_DIR = "dat"
_RESULTS_DIR = "out"
_LOGS_DIR = "logs"
_FINAL_FILE = "final.csv"
_SERVICE_HORIZON_FILE = "service.csv"
_ITERATION_TIME_FILE = "time.csv"
_FACILITIES_FILE = "facilities.csv"
_FINALDB = os.path.join(_RESULTS_DIR, _FINAL_FILE)
_SERVICEDB = os.path.join(_RESULTS_DIR, _SERVICE_HORIZON_FILE)
_TIMEDB = os.path.join(_RESULTS_DIR, _ITERATION_TIME_FILE)
_FACILITIESDB = os.path.join(_RESULTS_DIR, _FACILITIES_FILE)
