import requests
import threading
import enum
from pydantic import BaseModel
from misc.consts import SERVER_HOST, SERVER_PORT, CLIENT_HOST, CLIENT_PORT, LOGGER

from models.database import CarDB


class EventType(enum):
    OPEN_BARRIER = 1
    ADD_CAR = 2
    DELETE_CAR = 3
    BLOCK_CAR = 4
    UNBLOCK_CAR = 5

    TAKE_LOGS = 6
    TAKE_FRAME = 7
    TAKE_CARS = 8


class ServerJson(BaseModel):
    type: str
    data: dict

    class Config:
        schema_extra = {
            "example1": {
                "type": "add_car",
                "data": {"car_number": "A999AA777", "first_name": "Name"}
            },
            "example2": {
                "type": "delete_car",
                "data": {"car_number": "A999AA777"}
            },
            "example3": {
                "type": "block_car",
                "data": {"car_number": "A999AA777"}
            },
            "example4": {
                "type": "unblock_car",
                "data": {"car_number": "A999AA777"}
            }
        }


class SelfRequest:
    @staticmethod
    def add_car(car_number: str):
        result = requests.post(f"{CLIENT_HOST}:{CLIENT_PORT}/db/add_car",
                               json={"car_number": car_number})

    @staticmethod
    def delete_car(car_number: str):
        result = requests.delete(f"{CLIENT_HOST}:{CLIENT_PORT}/db/delete_car_by_number?number={car_number}")

    @staticmethod
    def block_car(car_number: str):
        result = requests.post(f"{CLIENT_HOST}:{CLIENT_PORT}/db/block_car_by_number?number={car_number}")

    @staticmethod
    def unblock_car(car_number: str):
        result = requests.post(f"{CLIENT_HOST}:{CLIENT_PORT}/db/unblock_car_by_number?number={car_number}")


class OnHeartBeat:
    def __init__(self):
        self.th = threading.Thread()
        self.allow_request = True

    def __thread_start(self):

        while self.allow_request:

            try:
                result = requests.get(f"{SERVER_HOST}:{SERVER_PORT}/OnHeartBeat", timeout=2)
                LOGGER.event(result)
            except Exception as ex:
                print(ex)
