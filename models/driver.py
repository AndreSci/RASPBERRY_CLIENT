from pydantic import BaseModel
from typing import List


class AboutCar(BaseModel):
    camera: str
    number: str
    date_time: str
    recognition_speed: float
    parsed: bool

    class Config:
        schema_extra = {
            "example": {
                "camera": "cam1",
                "number": "A111AA777",
                "date_time": "2023-05-23/10.43.09",
                "recognition_speed": 0.023
            }
        }


class RequestDriver(BaseModel):
    result: str
    desc: str
    data: List[AboutCar]

    class Config:
        schema_extra = {
            "example": {
                "result": "SUCCESS",
                "desc": "some words",
                "data": [
                    {
                        "camera": "cam1",
                        "number": "A111AA777",
                        "date_time": "2023-05-23/10.43.09",
                        "recognition_speed": 0.023
                    },
                    {
                        "camera": "cam2",
                        "number": "A112AA777",
                        "date_time": "2023-05-23/10.45.09",
                        "recognition_speed": 0.035
                    }
                ]
            }
        }