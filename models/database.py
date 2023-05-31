from pydantic import BaseModel
from typing import List


class CarDB(BaseModel):
    first_name: str
    car_number: str
    block: int

    class Config:
        schema_extra = {
            "example": {
                "first_name": "text",
                "car_number": "А999АА777",
                "block": 0
            }
        }
