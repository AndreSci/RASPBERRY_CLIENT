from pydantic import BaseModel
from typing import List


class CarDB(BaseModel):
    car_number: str

    class Config:
        schema_extra = {
            "example": {
                "car_number": "А999АА777"
            }
        }
