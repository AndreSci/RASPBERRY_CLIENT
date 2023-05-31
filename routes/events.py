from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.driver import RequestDriver
from database.sqlite3 import SQLCars
from control.barrier import BarrierClass

import sqlmodel

event_router = APIRouter(
    tags=["Events"]
)


DATA_BASE_EVENT = SQLCars()
BARRIER_CONTROL = BarrierClass()


@event_router.get("/number_on_frame")
async def number_on_frame(data: RequestDriver) -> dict:

    if data.data:

        ret_value = dict()

        for it in data.data:

            if await DATA_BASE_EVENT.get_car_by_number(it.number):
                ret_value[it.number] = "ALLOW"
                BARRIER_CONTROL.open(ret_value)
            else:
                ret_value[it.number] = "DISALLOW"

        return {
            "result": "SUCCESS",
            "desc": "",
            "data": ret_value
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="JSON is empty!"
    )


@event_router.get("/take_all")
async def retrieve_all_events() -> list:

    if DATA_BASE_EVENT:
        return DATA_BASE_EVENT

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Events does not exist"
    )