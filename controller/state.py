from enum import Enum

class ControllerState(str, Enum):
    INIT = "INIT"
    SPEC_READY = "SPEC_READY"
    TESTS_READY = "TESTS_READY"
    CODE_READY = "CODE_READY"
    EXECUTED = "EXECUTED"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
