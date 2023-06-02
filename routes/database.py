from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.database import CarDB
from database.sqlite3 import SQLCars
from misc.consts import LOGGER

import sqlmodel

db_router = APIRouter(
    tags=["Database"]
)

DATA_BASE = SQLCars()


@db_router.post("/add_car")
async def add_car(car: CarDB) -> dict:

    if car:
        result = await DATA_BASE.add_car(car.car_number)

        LOGGER.event(f"Действие с добавлением номера в БД: {result}")
        return {
            "result": result,
            "desc": "",
            "data": {}
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="JSON is empty!"
    )


@db_router.get("/cars")
async def retrieve_cars() -> dict:

    cars = await DATA_BASE.get_cars()

    if cars:
        return {
            "result": "SUCCESS",
            "desc": "",
            "data": cars
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="BASE is empty!"
    )


@db_router.get("/get_car_by_number")
async def retrieve_car_by_number(number: str) -> dict:
    cars = await DATA_BASE.get_car_by_number(number)

    if cars:
        return {
            "result": "SUCCESS",
            "desc": "",
            "data": cars
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="BASE is empty!"
    )


@db_router.delete("/delete_car_by_number")
async def delete_car_by_number(number: str) -> dict:
    result = await DATA_BASE.delete_car_by_number(number)

    if result:
        return {
            "result": "SUCCESS",
            "desc": f"Удалено полей: {result}",
            "data": {
                "car_number": number
            }
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Can't find number in DB!"
    )


@db_router.post("/block_car_by_number")
async def block_car_by_number(number: str) -> dict:
    result = await DATA_BASE.block_unblock_car_by_number(number, 1)

    if result:
        return {
            "result": "SUCCESS",
            "desc": f"Полей заблокировано: {result}",
            "data": {
                "car_number": number
            }
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Can't find number in DB!"
    )


@db_router.post("/unblock_car_by_number")
async def unblock_car_by_number(number: str) -> dict:
    result = await DATA_BASE.block_unblock_car_by_number(number, 0)

    if result:
        return {
            "result": "SUCCESS",
            "desc": f"Полей разблокировано: {result}",
            "data": {
                "car_number": number
            }
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Can't find number in DB!"
    )