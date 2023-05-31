from enum import Enum


class EventClass(Enum):
    NOTHING = 0
    OPEN_BARRIER = 1
    ADD_CAR = 2
    DEL_CAR = 3
    LICENSE_REQUEST = 4
    TAKE_CARS_LIST = 5
    TAKE_LOGS_BY_DAY = 6
    TAKE_FRAME = 7
    RESTART_DEVICE = 8
    RESTART_DRIVER = 9
    TAKE_CONFIG = 10
    WRITE_CONFIG = 11
    CHECK_VERSION = 12
    UPDATE_DEVICE = 13
    ROLLBACK_VERSION = 14


var = {
    'RESULT': 'SUCCESS',
    'DESC': '',
    'DATA': {
        'message_id': int,  # 2023121214553355555
        'event': int,
        'data': {}
    }
}
