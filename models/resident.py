from pydantic import BaseModel
from typing import List


class Resident(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str
    email: str
    car_number: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "text",
                "last_name": "text",
                "middle_name": "text",
                "phone_number": "+79991112233",
                "email": "test@tgmail.com",
                "car_number": "А111АА777"
            }
        }
